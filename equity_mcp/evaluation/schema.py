"""
The contract for a metrics/<role>.yaml rubric file.

Every rubric is hand-written and every rubric is sent, question by question, to
a paid API, so a typo has to fail at load time rather than as a 422 halfway
through a backfill. Pydantic does that here, and only here, in the same way
langchain_bridge uses it only to build tool argument schemas.

A rubric has two blocks that are scored and stored separately and never
averaged together:

``conviction``
    What the agent concluded. This holds the shared five-way stance Choice
    (in _shared.yaml), a conviction level, and the role's own domain metrics:
    5-level Scores such as profitability or governance, oriented 0 = very
    unfavourable to 4 = very favourable for a long investor.

``alignment``
    How well the output followed its prompt. This holds deterministic checks,
    run in code, and grouped Jev questions.

Constraints that come from Jev itself rather than taste:

- Question ids are never sent to the model, so ``instructions`` must say the
  whole judgment.
- Score has no abstain option. Abstention comes from a gate Noul, for requests,
  or a keyword coverage check, for domain metrics.
- Score levels are 0-based on the wire: ``criteria[0]`` is level 0.
- A Choice may have at most 255 options and a Score 2–10 levels.
"""

from __future__ import annotations

import re
from typing import Annotated, Literal, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

STANCES: tuple[str, ...] = ("STRONG SELL", "SELL", "HOLD", "BUY", "STRONG BUY")
"""The five-way stance every agent is placed on. Order is bearish → bullish."""

STANCE_VALUES: dict[str, int] = {s: v for s, v in zip(STANCES, (-2, -1, 0, 1, 2))}

BUILTIN_SECTIONS: frozenset[str] = frozenset({"full", "raw", "preamble"})
"""Sections every report has without declaring them.

``full`` is the report with its leading chatter stripped, ``raw`` is the text
exactly as the agent wrote it, and ``preamble`` is only the stripped chatter.
The head of research's "All 13 specialist reports are in context" claim lives
in the preamble, which is why it is kept at all.
"""

CONTEXT_KEYS: frozenset[str] = frozenset({"crossagent"})
"""Extra state blocks a request can ask for, built in code rather than read from the report."""

MAX_QUESTIONS_PER_REQUEST = 6
DOMAIN_LEVELS = 5

ExtractId = str
SectionId = str


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


# ── Report structure ──────────────────────────────────────────────────────────


class Section(_Strict):
    """A named slice of a report, selected by a case-insensitive heading regex."""

    heading: str
    all_matches: bool = False
    """Concatenate every matching section rather than taking the first."""
    max_chars: int = Field(6000, ge=200, le=12000)

    @field_validator("heading")
    @classmethod
    def _compiles(cls, v: str) -> str:
        re.compile(v, re.IGNORECASE)
        return v


class Extract(_Strict):
    """A value pulled out of the report by code, never by the model.

    ``values`` makes it an enum extract: it is matched case-insensitively and
    longest-first, so ``Strong Buy`` wins over ``Buy``. It looks first in the
    section's heading line, then in the first ``body_chars`` of its body.
    ``pattern`` makes it a numeric extract, with the first capture group parsed
    as ``type``.
    """

    section: SectionId
    anchor: str | None = None
    """Regex. When set, search only the ``body_chars`` after its first match in the section
    (e.g. ``composite`` to find quant's ``**Composite Quant Score: NEUTRAL**`` line)."""
    values: list[str] | None = None
    aliases: dict[str, str] = Field(default_factory=dict)
    """Alternative spellings mapped to a canonical value, e.g. ``Above: Tracking Above``."""
    pattern: str | None = None
    type: Literal["enum", "int", "float"] = "enum"
    range: tuple[float, float] | None = None
    body_chars: int = Field(400, ge=0, le=4000)

    @model_validator(mode="after")
    def _one_kind(self) -> Extract:
        if (self.values is None) == (self.pattern is None):
            raise ValueError("an extract needs exactly one of `values` or `pattern`")
        if self.values is not None:
            if self.type != "enum":
                raise ValueError("`values` extracts are type enum")
            missing = set(self.aliases.values()) - set(self.values)
            if missing:
                raise ValueError(f"aliases point at unknown values: {sorted(missing)}")
        else:
            if self.type == "enum":
                raise ValueError("`pattern` extracts must be type int or float")
            if re.compile(self.pattern).groups < 1:
                raise ValueError("`pattern` needs a capture group")
        if self.anchor is not None:
            re.compile(self.anchor, re.IGNORECASE)
        return self


# ── Questions ─────────────────────────────────────────────────────────────────


class _QuestionBase(_Strict):
    instructions: str = Field(min_length=20)
    dimension: str = "general"
    weight: float = Field(1.0, ge=0)
    veto: bool = False
    """A failed veto metric is reported separately and is never averaged away."""


class NoulCriteria(_Strict):
    true: str
    false: str


class NoulQ(_QuestionBase):
    type: Literal["noul"]
    criteria: NoulCriteria | None = None
    good_when: bool = True
    """Which answer is the good one. ``False`` turns "is there injected text?" into a pass on *no*."""
    threshold: float = Field(0.5, gt=0, lt=1)

    @field_validator("criteria", mode="before")
    @classmethod
    def _yaml_bool_keys(cls, v: object) -> object:
        # YAML reads an unquoted `true:` key as the boolean True.
        if isinstance(v, dict):
            return {str(k).lower() if isinstance(k, bool) else k: val for k, val in v.items()}
        return v


class ScoreQ(_QuestionBase):
    type: Literal["score"]
    criteria: list[str] = Field(min_length=2, max_length=10)
    min_level: int | None = None
    """0-based level at or above which the metric passes. Defaults to the middle level."""

    @model_validator(mode="after")
    def _min_level_in_range(self) -> ScoreQ:
        if self.min_level is not None and not 0 <= self.min_level < len(self.criteria):
            raise ValueError(f"min_level {self.min_level} outside 0..{len(self.criteria) - 1}")
        return self

    @property
    def pass_level(self) -> int:
        return self.min_level if self.min_level is not None else len(self.criteria) // 2


class ChoiceQ(_QuestionBase):
    type: Literal["choice"]
    criteria: dict[str, str] = Field(min_length=2, max_length=255)
    value_map: dict[str, float] | None = None
    """Option → 0..1 quality value. Without it, a Choice is extraction-only and should be weight 0."""
    cross_check: ExtractId | None = None
    """Extract id whose code-side value is compared with the Jev choice."""
    order_check: bool = False

    @model_validator(mode="after")
    def _value_map_keys(self) -> ChoiceQ:
        if self.value_map is not None:
            unknown = set(self.value_map) - set(self.criteria)
            if unknown:
                raise ValueError(f"value_map has unknown options: {sorted(unknown)}")
        if self.weight > 0 and self.value_map is None:
            raise ValueError("a weighted choice needs a value_map to be scored")
        return self


Question = Annotated[Union[NoulQ, ScoreQ, ChoiceQ], Field(discriminator="type")]


class Request(_Strict):
    """Questions that share one state, sent in one Jev call."""

    id: str
    state: list[SectionId] = Field(min_length=1)
    context: list[str] = Field(default_factory=list)
    gate: str | None = None
    """A Noul in this request. When it fails, its siblings are recorded as low_evidence."""
    questions: dict[str, Question] = Field(min_length=1, max_length=MAX_QUESTIONS_PER_REQUEST)

    @model_validator(mode="after")
    def _gate_is_noul(self) -> Request:
        if self.gate is not None:
            q = self.questions.get(self.gate)
            if q is None or q.type != "noul":
                raise ValueError(f"gate '{self.gate}' must be a noul question in request '{self.id}'")
        unknown = set(self.context) - CONTEXT_KEYS
        if unknown:
            raise ValueError(f"unknown context keys {sorted(unknown)}; allowed: {sorted(CONTEXT_KEYS)}")
        return self


# ── Deterministic checks ──────────────────────────────────────────────────────


CheckKind = Literal[
    "sections_present",        # sections: [...]
    "extract_ok",              # extract: id
    "table_present",           # section, min_rows, columns?, row_labels?
    "min_matches",             # section, pattern, min
    "min_list_items",          # section, min, max?
    "regex_absent",            # section, pattern
    "not_degenerate",          # (none)
    "price_target_consistent", # section
    "fraud_override",          # extract: portfolio action extract id
    "failures_acknowledged",   # section
    "position_size_band",      # section, extract: consensus/conviction extract id
]


class DeterministicCheck(_Strict):
    id: str
    kind: CheckKind
    dimension: str = "compliance"
    weight: float = Field(1.0, ge=0)
    veto: bool = False
    section: SectionId | None = None
    sections: list[SectionId] | None = None
    extract: ExtractId | None = None
    pattern: str | None = None
    min: int | None = None
    max: int | None = None
    min_rows: int | None = None
    columns: list[str] | None = None
    row_labels: list[str] | None = None

    @model_validator(mode="after")
    def _required_fields(self) -> DeterministicCheck:
        need = {
            "sections_present": ("sections",),
            "extract_ok": ("extract",),
            "table_present": ("section", "min_rows"),
            "min_matches": ("section", "pattern", "min"),
            "min_list_items": ("section", "min"),
            "regex_absent": ("section", "pattern"),
            "price_target_consistent": ("section",),
            "fraud_override": ("extract",),
            "failures_acknowledged": ("section",),
            "position_size_band": ("section",),
        }.get(self.kind, ())
        missing = [f for f in need if getattr(self, f) is None]
        if missing:
            raise ValueError(f"check '{self.id}' ({self.kind}) needs {missing}")
        if self.pattern is not None:
            re.compile(self.pattern, re.IGNORECASE)
        return self


# ── Conviction block ──────────────────────────────────────────────────────────


class DomainMetric(_Strict):
    """One 5-level favourability Score, sent only if code finds evidence for it."""

    label: str
    section: list[SectionId] = Field(min_length=1)
    """Tried in order. The first that resolves wins; ``full`` is the usual last resort."""
    evidence_terms: list[str] = Field(min_length=1)
    instructions: str = Field(min_length=20)
    criteria: list[str] = Field(min_length=DOMAIN_LEVELS, max_length=DOMAIN_LEVELS)

    @field_validator("section", mode="before")
    @classmethod
    def _listify(cls, v: object) -> object:
        return [v] if isinstance(v, str) else v


class Conviction(_Strict):
    native_rating: ExtractId | None = None
    """The agent's own headline enum, mapped to a stance through ``native_to_stance``."""
    native_to_stance: dict[str, str | None] = Field(default_factory=dict)
    native_conviction: ExtractId | None = None
    """An extract the agent reports as Low/Medium/High, compared with the conviction_level Score."""
    domain_metrics: dict[str, DomainMetric] = Field(min_length=4)

    @field_validator("native_to_stance")
    @classmethod
    def _valid_stances(cls, v: dict[str, str | None]) -> dict[str, str | None]:
        bad = {k: s for k, s in v.items() if s is not None and s not in STANCES}
        if bad:
            raise ValueError(f"native_to_stance targets must be one of {STANCES}: {bad}")
        return v


class Alignment(_Strict):
    deterministic_checks: list[DeterministicCheck] = Field(default_factory=list)
    requests: list[Request] = Field(default_factory=list)


class Background(_Strict):
    mandate: str = Field(min_length=40)
    required_output: str = Field(min_length=40)


# ── Files ─────────────────────────────────────────────────────────────────────


class Rubric(_Strict):
    """A metrics/<role>.yaml file."""

    role: str
    rubric_version: int = Field(ge=1)
    pass_: Literal[1, 2] = Field(alias="pass")
    includes: list[str] = Field(default_factory=lambda: ["_shared"])
    source_prompt: str
    source_prompt_sha256: str
    calibrated: bool = False
    background: Background
    sections: dict[SectionId, Section] = Field(default_factory=dict)
    extract: dict[ExtractId, Extract] = Field(default_factory=dict)
    conviction: Conviction
    alignment: Alignment

    @model_validator(mode="after")
    def _references_resolve(self) -> Rubric:
        sections = set(self.sections) | BUILTIN_SECTIONS
        clash = set(self.sections) & BUILTIN_SECTIONS
        if clash:
            raise ValueError(f"sections may not redefine built-ins: {sorted(clash)}")

        def need_section(where: str, sid: str | None) -> None:
            if sid is not None and sid not in sections:
                raise ValueError(f"{where}: unknown section '{sid}'")

        def need_extract(where: str, eid: str | None) -> None:
            if eid is not None and eid not in self.extract:
                raise ValueError(f"{where}: unknown extract '{eid}'")

        for eid, ex in self.extract.items():
            need_section(f"extract.{eid}", ex.section)
        c = self.conviction
        need_extract("conviction.native_rating", c.native_rating)
        need_extract("conviction.native_conviction", c.native_conviction)
        if c.native_rating is not None:
            values = set(self.extract[c.native_rating].values or [])
            unmapped = values - set(c.native_to_stance)
            if unmapped:
                raise ValueError(f"native_to_stance is missing {sorted(unmapped)}")
        for mid, m in c.domain_metrics.items():
            for sid in m.section:
                need_section(f"domain_metrics.{mid}", sid)
        for chk in self.alignment.deterministic_checks:
            need_section(f"check.{chk.id}", chk.section)
            for sid in chk.sections or []:
                need_section(f"check.{chk.id}", sid)
            need_extract(f"check.{chk.id}", chk.extract)
        for req in self.alignment.requests:
            for sid in req.state:
                need_section(f"request.{req.id}", sid)
            for qid, q in req.questions.items():
                if isinstance(q, ChoiceQ):
                    need_extract(f"request.{req.id}.{qid}", q.cross_check)
        return self


class SharedConviction(_Strict):
    """The questions asked identically of every agent, so answers compare across agents."""

    state: list[SectionId] = Field(default_factory=lambda: ["full"])
    stance_gate: NoulQ
    stance: ChoiceQ
    conviction_level: ScoreQ

    @model_validator(mode="after")
    def _exact_stances(self) -> SharedConviction:
        if tuple(self.stance.criteria) != STANCES:
            raise ValueError(f"stance criteria must be exactly {STANCES}, in that order")
        if len(self.conviction_level.criteria) != 3:
            raise ValueError("conviction_level must have 3 levels: Low, Medium, High")
        return self


class SharedRubric(_Strict):
    """metrics/_shared.yaml"""

    shared_version: int = Field(ge=1)
    conviction: SharedConviction
    alignment: Alignment

    @model_validator(mode="after")
    def _builtin_sections_only(self) -> SharedRubric:
        for req in self.alignment.requests:
            bad = set(req.state) - BUILTIN_SECTIONS
            if bad:
                raise ValueError(f"_shared request '{req.id}' may only use built-in sections, not {sorted(bad)}")
        for chk in self.alignment.deterministic_checks:
            for sid in [chk.section, *(chk.sections or [])]:
                if sid is not None and sid not in BUILTIN_SECTIONS:
                    raise ValueError(f"_shared check '{chk.id}' may only use built-in sections")
            if chk.extract is not None:
                raise ValueError(f"_shared check '{chk.id}' may not reference role extracts")
        return self
