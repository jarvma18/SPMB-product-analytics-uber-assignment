# lib/charts.py
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def bar_comparison(label1, value1, label2, value2, title, ylabel):
  plt.figure(figsize=(6, 4))
  plt.bar([label1, label2], [value1, value2], color=['#1f77b4', '#ff7f0e'])
  plt.title(title)
  plt.ylabel(ylabel)
  plt.tight_layout()
  plt.show()

def boxplot_series(series1, label1, series2, label2, title, ylabel):
  import pandas as pd
  data = pd.DataFrame({
    ylabel: pd.concat([series1, series2]),
    'Group': [label1] * len(series1) + [label2] * len(series2)
  })
  plt.figure(figsize=(6, 4))
  sns.boxplot(x='Group', y=ylabel, data=data)
  plt.title(title)
  plt.tight_layout()
  plt.show()
