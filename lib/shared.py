import pandas as pd
from scipy.stats import ttest_ind

def run_t_test(first_sample: pd.Series, first_sample_title: str, second_sample: pd.Series, second_sample_title: str):
  t_stat, p_value = ttest_ind(first_sample, second_sample, equal_var=False)
  print(f"Mean {first_sample_title}: {first_sample.mean()}, Mean {second_sample_title}: {second_sample.mean()}")
  print(f"t = {t_stat:.3f}, p = {p_value:.3e}")
  print("Statistically significant at 5%" if p_value < 0.05 else "Not statistically significant")