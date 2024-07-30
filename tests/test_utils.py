import json
import unittest
from unittest.mock import MagicMock, mock_open, patch
from src.utils import transaction_list_amount, open_csv_data, open_excel_data

from unittest.mock import patch, mock_open
from tests.conftest import test_info_xlcx, test_info_csv


def test_get_info_transaction(test_info_csv, test_info_xlcx):
    info_csv = list(open_csv_data("../data/transactions.csv"))
    assert info_csv[0] == test_info_csv

    info_xlsx = list(open_excel_data("../data/transactions_excel.xlsx"))
    assert info_xlsx[0] == test_info_xlcx


@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_get_info_transactions_csv_xlsx(mock_file):
    assert open("../Data/test_transactions_csv.csv").read() == "data"
    mock_file.assert_called_with("../Data/test_transactions_csv.csv")

    assert open("../data/test_transactions_excel.xlsx").read() == "data"
    mock_file.assert_called_with("../data/test_transactions_excel.xlsx")
