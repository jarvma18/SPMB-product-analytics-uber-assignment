import pandas as pd
from typing import Union, List

def read_csv_file(
  file_path: str,
  delimiter: str = ';',
  encoding: str = 'utf-8',
  parse_dates: Union[bool, List[str]] = False
) -> pd.DataFrame:
  """
  Reads a CSV file into a pandas DataFrame.

  Parameters:
    file_path (str): Path to the CSV file.
    delimiter (str): Delimiter used in the CSV (default is semi-comma).
    encoding (str): File encoding (default is 'utf-8').
    parse_dates (bool or list of str): Automatically parse dates (default is False).

  Returns:
    pd.DataFrame: DataFrame with the contents of the CSV.
  """
  try:
    df: pd.DataFrame = pd.read_csv(
      file_path,
      delimiter=delimiter,
      encoding=encoding,
      parse_dates=parse_dates,
      converters={"total_driver_payout": lambda x: float(x.replace(",", "."))}
    )
    print(f"CSV loaded successfully. Shape: {df.shape}\n")
    return df
  except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
  except pd.errors.ParserError as e:
    print(f"Parsing error: {e}")
  except Exception as e:
    print(f"Unexpected error: {e}")

  return pd.DataFrame()  # Return empty DataFrame on failure
df = pd.read_csv("data/uber_dataset.csv", converters={"total_driver_payout": lambda x: float(x.replace(",", "."))})
