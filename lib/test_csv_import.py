import unittest
import pandas as pd
import os
import tempfile
from csv_import import read_csv_file

class TestReadCsvFile(unittest.TestCase):

  def setUp(self):
    self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, newline='', suffix='.csv')
    self.temp_file.write("id,name,date\n1,Alice,2023-01-01\n2,Bob,2023-01-02\n")
    self.temp_file.close()
    self.file_path = self.temp_file.name

  def tearDown(self):
    os.remove(self.temp_file.name)

  def test_read_valid_csv(self):
    df = read_csv_file(self.file_path)
    self.assertIsInstance(df, pd.DataFrame)
    self.assertEqual(df.shape, (2, 3))
    self.assertListEqual(list(df.columns), ['id', 'name', 'date'])

  def test_read_with_parse_dates(self):
    df = read_csv_file(self.file_path, parse_dates=['date'])
    self.assertTrue(pd.api.types.is_datetime64_any_dtype(df['date']))

  def test_file_not_found(self):
    df = read_csv_file("nonexistent.csv")
    self.assertTrue(df.empty)

  def test_invalid_csv_format(self):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as bad_file:
      bad_file.write("id,name,date\n1,Alice,2023-01-01\n2,Bob,\"unterminated quote\n")
      bad_file_path = bad_file.name

    df = read_csv_file(bad_file_path)
    self.assertTrue(df.empty)
    os.remove(bad_file_path)


if __name__ == '__main__':
  unittest.main()
