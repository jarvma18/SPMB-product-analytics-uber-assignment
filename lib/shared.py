import pandas as pd
from scipy.stats import ttest_ind
from lib.charts import bar_comparison, boxplot_series

def run_t_test(first_sample: pd.Series, first_sample_title: str, second_sample: pd.Series, second_sample_title: str):
  t_stat, p_value = ttest_ind(first_sample, second_sample, equal_var=False)
  first_mean = round(first_sample.mean(), 2)
  second_mean = round(second_sample.mean(), 2)

  print(f"Mean {first_sample_title}: {first_mean}, Mean {second_sample_title}: {second_mean}")
  print(f"t = {t_stat:.3f}, p = {p_value:.6f}")
  print("Statistically significant\n" if p_value < 0.05 else "Not statistically significant\n")

  bar_comparison(
    first_sample_title, first_mean,
    second_sample_title, second_mean,
    title=f"t-test: {first_sample_title} vs {second_sample_title}",
    ylabel="Mean"
  )

  boxplot_series(
    first_sample, first_sample_title,
    second_sample, second_sample_title,
    title=f"t-test (distribution): {first_sample_title} vs {second_sample_title}",
    ylabel="Value"
  )

def print_difference(first_value: float, other_value: float, first_title: str, other_title: str, print_dollar: bool):
  difference: float = round(abs(first_value - other_value), 2)
  print_labeled_amount(first_title, first_value, print_dollar)
  print_labeled_amount(other_title, other_value, print_dollar)
  print_labeled_amount('Difference', difference, print_dollar)
  print('\n')
  bar_comparison(first_title, first_value, other_title, other_value, 'Value Comparison', 'Value')

def print_higher_number_choice(first_choice: str, first_choice_sum: float, other_choice: str, other_choice_sum: float):
  first_choice_print: str = first_choice + ' has higher number\n'
  other_choice_print: str = other_choice + ' has higher number\n'
  first_choice_has_higher_number: bool = first_choice_sum > other_choice_sum;
  print(first_choice, ':', first_choice_sum, 'vs', other_choice, ':', other_choice_sum)
  print(first_choice_print if first_choice_has_higher_number else other_choice_print)

  bar_comparison(
    first_choice, first_choice_sum,
    other_choice, other_choice_sum,
    title="Comparison of Totals",
    ylabel="Total"
  )

def print_labeled_amount(title: str, value: float, add_dollar):
  if add_dollar:
    print(title, ':', round(value, 2), '$')
  else:
    print(title, ':', round(value, 2))
