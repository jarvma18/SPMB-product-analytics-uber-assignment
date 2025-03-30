from lib.csv_import import read_csv_file
import pandas as pd
from scipy.stats import ttest_ind

def main():
  df = read_csv_file("data/uber_dataset.csv")

main()