##v_rubic_questions##
Hyperparameters displayed are breakdown by `role` folder level:
a. select these fields and sorted by level in ascending order=> level 1- `block`, level 2- `dimension`, level 3- `kind`, level 4- `question_id`, level 5-   `instructions`
b. if kind=score, display `n_levels` as level of scoring (e.g. 4 means score of 0 to 4),` pass_level` as threshold level of passing (e.g. 2 means need a score of 2 to pass)


##v_rubic_criteria##
Hyperparameters displayed are breakdown by `role` folder level:
a. select these fields and sorted by level in ascending order=> level 1- `block` (reference key to `v_rubic_questions.block`),  level 2- `kind` (reference key to `v_rubic_questions.kind`), level 3- `question_id` (reference key to `v_rubic_questions.question_id`)
b. when `kind`=score, display out for each question_id what does each score meant (`option_key`,`criterion`)
c. when `kind`=choice, display out for each question_id what does each choice meant (`option_key`,`criterion`)
d. when `kind`=noul, display out for each question_id what does each decision (true/ false) meant (`option_key`,`criterion`)

##v_rubic_metrics##
Hyperparameters displayed are breakdown by `role` folder level:
a. select these fields and sorted by level in ascending order=> level 1- `block` (reference key to `v_rubic_criteria.block`), level 2- `dimension` (reference key to `v_rubic_questions.dimension`), level 3- `kind` (reference key to `v_rubic_criteria.kind`), level 4- `metric_id` (reference key to `v_rubic_questions.question_id`), level 4- `label`, level 5- `description`