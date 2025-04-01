import pandas as pd
from scipy.stats import ttest_ind

def run_t_test(first_sample: pd.Series, first_sample_title: str, second_sample: pd.Series, second_sample_title: str):
  t_stat, p_value = ttest_ind(first_sample, second_sample, equal_var=False)
  print(f"Mean {first_sample_title}: {first_sample.mean()}, Mean {second_sample_title}: {second_sample.mean()}")
  print(f"t = {t_stat:.3f}, p = {p_value:.6f}")
  print("Statistically significant at 5%\n" if p_value < 0.05 else "Not statistically significant\n")

def print_difference(first_value: float, other_value: float):
  difference: float = abs(first_value - other_value)
  print('Difference:', difference, '\n')

def print_higher_number_choice(first_choice: str, first_choice_sum: float, other_choice: str, other_choice_sum: float):
  first_choice_print: str = first_choice + ' has higher number\n'
  other_choice_print: str = other_choice + ' has higher number\n'
  first_choice_has_higher_number: bool = first_choice_sum > other_choice_sum;
  print(first_choice, ':', first_choice_sum, 'vs', other_choice, ':', other_choice_sum)
  print(first_choice_print if first_choice_has_higher_number else other_choice_print)

def print_labeled_amount(title: str, value: float, add_dollar):
  if add_dollar:
    print(title, ':', value, '$')
  else:
    print(title, ':', value)
