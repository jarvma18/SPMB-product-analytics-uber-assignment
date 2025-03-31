import pandas as pd
from scipy.stats import ttest_ind

def run_t_test(first_sample: pd.Series, first_sample_title: str, second_sample: pd.Series, second_sample_title: str):
  t_stat, p_value = ttest_ind(first_sample, second_sample, equal_var=False)
  print(f"Mean {first_sample_title}: {first_sample.mean()}, Mean {second_sample_title}: {second_sample.mean()}")
  print(f"t = {t_stat:.3f}, p = {p_value:.6f}")
  print("Statistically significant at 5%\n" if p_value < 0.05 else "Not statistically significant\n")

def print_difference(firstValue: float, otherValue: float):
  difference: float = abs(firstValue - otherValue)
  print('Difference:', difference, '\n')

def print_higher_number_choice(firstChoice: str, firstChoiceSum: float, otherChoice: str, otherChoiceSum: float):
  firstChoicePrint: str = firstChoice + ' has higher number\n'
  otherChoicePrint: str = otherChoice + ' has higher number\n'
  firstChoiceHasHigherNumber: bool = firstChoiceSum > otherChoiceSum;
  print(firstChoice, ':', firstChoiceSum, 'vs', otherChoice, ':', otherChoiceSum)
  print(firstChoicePrint if firstChoiceHasHigherNumber else otherChoicePrint)

def print_labeled_amount(title: str, value: float, addDollar):
  if addDollar:
    print(title, ':', value, '$')
  else:
    print(title, ':', value)