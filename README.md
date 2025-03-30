# SPMB Product Analytics Uber Assignment

## 1. Compare commuting hours versus non-commuting hours in the control group (i.e., with 2-minute wait times)
Hint: For this exercise you need to select a subsample of the dataset: the observations in the control group, i.e., the observations where the variable “treat” = FALSE. Then, within the “treat” = FALSE subsample, we can run t-tests between the observations with the variable “commute” = TRUE and observations with the variable “commute” = FALSE.

## 2. Estimate the effect of extending waiting times from 2 minutes (control group) to 5 minutes (treatment group) separately for commuting and non-commuting hours.
Hint:  For parts 1 to 11 you need to compare treatment and control subsamples only during commuting hours so we limit the observations to “commute” = TRUE. We run t-tests between two subsamples of the observations with “commute” = TRUE: “treat” = TRUE – 5 minute waiting – and “treat” = FALSE – 2 minute waiting.
