# lib/charts.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from datetime import datetime

sns.set(style="whitegrid")

def bar_comparison(label1, value1, label2, value2, title, ylabel, save_as=None):
  plt.figure(figsize=(8, 6))
  plt.bar([label1, label2], [value1, value2], color=['#1f77b4', '#ff7f0e'])
  plt.title(title)
  plt.ylabel(ylabel)
  plt.tight_layout()

  save_path = save_as or _autogen_path(title, suffix="bar")
  _save_figure(save_path)
  plt.show()

def boxplot_series(series1, label1, series2, label2, title, ylabel, save_as=None):
  data = pd.DataFrame({
    ylabel: pd.concat([series1, series2]),
    'Group': [label1] * len(series1) + [label2] * len(series2)
  })

  plt.figure(figsize=(8, 6))
  sns.boxplot(x='Group', y=ylabel, data=data)
  plt.title(title)
  plt.tight_layout()

  save_path = save_as or _autogen_path(title, suffix="boxplot")
  _save_figure(save_path)
  plt.show()

def _save_figure(path: str):
  os.makedirs(os.path.dirname(path), exist_ok=True)
  plt.savefig(path)


def _autogen_path(title: str, suffix: str):
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  slug = (
    title.lower()
    .replace(" ", "_")
    .replace("(", "")
    .replace(")", "")
    .replace(":", "")
    .replace("-", "_")
  )
  filename = f"{timestamp}_{slug}_{suffix}.png"
  return os.path.join("plots", filename)