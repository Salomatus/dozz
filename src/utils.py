import json
import os

import pandas as pd
import csv
from src.logger import setup_logger


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_1)


def transaction_list_amount(json_file_path: str) -> list[dict]:
    """ Функция которая, принимает путь до JSON-файла возвращает данные с финансовых транзакций """

    try:
        logger.info(f'открываем json файл {json_file_path}')
        with open(json_file_path, "r", ecoding="utf-8") as file:
            list_amount = json.load(file)
            logger.info(f"Проверяeм, что файл {json_file_path} не пустой")
            if isinstance(list_amount, list):
                return list_amount
            else:
                logger.info(f'Возвращаем пустой словарь, если файл {json_file_path} пустой')
                return []

    except Exception:
        logger.error(f'Произошла ошибка')
        return []

def open_csv_data(file: str) -> list[dict]:
        """Функция считывающая cvs файл и возвращающая список словарей"""
        with open(file, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            header_in = next(reader)
            result = []
            for index in reader:
                row_dict = {
                    "id": index[header_in.index("id")],
                    "state": index[header_in.index("state")],
                    "date": index[header_in.index("date")],
                    "operationAmount": {
                        "amount": index[header_in.index("amount")],
                        "currency": {
                            "name": index[header_in.index("currency_name")],
                            "code": index[header_in.index("currency_code")],
                        },
                    },
                    "description": index[header_in.index("description")],
                    "from": index[header_in.index("from")],
                    "to": index[header_in.index("to")],
                }
                result.append(row_dict)
            return result


def open_excel_data(file: str) -> list[dict]:
        """Функция считывает файл в формат excel и возвращающая список словарей"""
        df = pd.read_excel(file)
        result = []
        rows_count = len(df)
        for i in range(0, rows_count):
            row_dict = {
                "id": df.at[i, "id"],
                "state": df.at[i, "state"],
                "date": df.at[i, "date"],
                "operationAmount": {
                    "amount": df.at[i, "amount"],
                    "currency": {
                        "name": df.at[i, "currency_name"],
                        "code": df.at[i, "currency_code"],
                    },
                },
                "description": df.at[i, "description"],
                "from": df.at[i, "from"],
                "to": df.at[i, "to"],
            }
            result.append(row_dict)
        return result

