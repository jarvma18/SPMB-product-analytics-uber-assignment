import unittest
from unittest.mock import patch, call
import pandas as pd
from lib.shared import run_t_test, print_difference, print_higher_number_choice, print_labeled_amount
from lib.charts import bar_comparison, boxplot_series

class TestAnalysisFunctions(unittest.TestCase):
  @patch("shared.bar_comparison")
  @patch("shared.boxplot_series")
  @patch("builtins.print")
  def test_run_t_test_significant_difference(self, mock_print, mock_boxplot, mock_barplot):
    sample1: pd.Series = pd.Series([1, 2, 3, 4, 5])
    abnormal_sample: pd.Series = pd.Series([10, 11, 12, 13, 14])
    run_t_test(sample1, "Group A", abnormal_sample, "Group B")
    mock_print.assert_any_call("Mean Group A: 3.0, Mean Group B: 12.0")
    self.assertTrue(any("Statistically significant" in str(c[0]) for c in mock_print.call_args_list))
    mock_barplot.assert_called_once()
    mock_boxplot.assert_called_once()

  @patch("shared.bar_comparison")
  @patch("shared.boxplot_series")
  @patch("builtins.print")
  def test_run_t_test_not_significant_difference(self, mock_print, mock_boxplot, mock_barplot):
    sample1: pd.Series = pd.Series([1, 2, 3, 4, 5])
    same_like_sample1_sample: pd.Series = pd.Series([1.1, 2.1, 3.1, 4.1, 5.1])
    run_t_test(sample1, "Group A", same_like_sample1_sample, "Group B")
    mock_print.assert_any_call("Mean Group A: 3.0, Mean Group B: 3.1")
    self.assertTrue(any("Not statistically significant" in str(c[0]) for c in mock_print.call_args_list))
    mock_barplot.assert_called_once()
    mock_boxplot.assert_called_once()

  @patch("shared.bar_comparison")
  @patch("builtins.print")
  def test_print_difference_with_dollar(self, mock_print, mock_barplot):
    print_difference(100.0, 80.0, "A", "B", True)
    expected_calls: list = [
      call("A", ':', 100.0, '$'),
      call("B", ':', 80.0, '$'),
      call("Difference", ':', 20.0, '$'),
      call('\n')
    ]
    # Flatten calls for validation
    flat_calls = [tuple(arg for arg in c[0]) for c in mock_print.call_args_list if c[0]]
    for ec in expected_calls:
      self.assertIn(ec, flat_calls)
    mock_barplot.assert_called_once()

  @patch("shared.bar_comparison")
  @patch("builtins.print")
  def test_print_higher_number_choice(self, mock_print, mock_barplot):
    print_higher_number_choice("Option A", 150.0, "Option B", 120.0)
    mock_print.assert_any_call("Option A", ':', 150.0, 'vs', "Option B", ':', 120.0)
    mock_print.assert_any_call("Option A has higher number\n")
    mock_barplot.assert_called_once()

  @patch("builtins.print")
  def test_print_labeled_amount_with_and_without_dollar(self, mock_print):
    print_labeled_amount("Test", 123.456, True)
    mock_print.assert_called_with("Test", ':', 123.46, '$')
    mock_print.reset_mock()
    print_labeled_amount("Test", 123.456, False)
    mock_print.assert_called_with("Test", ':', 123.46)

if __name__ == '__main__':
  unittest.main()