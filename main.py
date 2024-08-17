from src.masks import mask_card, mask_account

import re

import os

import pandas as pd

from src.processing import get_date_sorted, get_dictionary_key

from src.generators import filter_by_currency, transactions_descriptions

from src.utils import transaction_list_amount, open_csv_data, open_excel_data

from src.Search_trans import search_transactions, list_transactions

PATH_TO_FILE_JSON = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transaction_excel.xlsx")

def main():
    """Функция, которая отвечает за основную логику проекта и связывает функции между собой."""
    while True:
        menu_item = input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
        )
        if menu_item == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = transaction_list_amount(PATH_TO_FILE_JSON)
            break
        elif menu_item == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = open_csv_data(PATH_TO_FILE_CSV)
            break
        elif menu_item == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = open_excel_data(PATH_TO_FILE_EXCEL)
            break
        else:
            print("Такого пункта в меню нет, попробуйте еще раз.")

    state_list = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        state = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
"""
        ).upper()

        if state not in state_list:
            print(f'Статус операции "{state}" недоступен.')
        else:
            break
        filtered_transactions = get_dictionary_key(transactions, state)
        date_sort = input("Отсортировать операции по дате? Да/Нет. ").lower()
        if date_sort == "да":
            if input("Отсортировать по возрастанию или по убыванию? ").lower() == "по возрастанию":
                date_flag = False
            else:
                date_flag = True
            filtered_transactions = get_date_sorted(filtered_transactions, date_flag)
        filter_by_rub = input("Выводить только рублевые транзакции? Да/Нет ")
        if filter_by_rub.lower() == "да":
            rub_transactions = filter_by_currency(filtered_transactions, "RUB")
            filtered_transactions = list(rub_transactions)[:-1]
        filter_by_word = input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
        if filter_by_word.lower() == "да":
            filter_by_word = input("Введите слово: ")

            transactions = list_transactions
            for filter_type, filter_value in list_transactions.items():
                if filter_type == "state":
                    transactions = get_dictionary_key(transactions, filter_value)
                elif filter_type == "date":
                    transactions = get_date_sorted(transactions, filter_value)
                elif filter_type == "currency":
                    transactions = [
                        txn
                        for txn in transactions
                        if txn.get("operationAmount", {}).get("currency", {}).get("code") == filter_value
                    ]
                elif filter_type == "description":
                    transactions = search_transactions(transactions, filter_value)

            if not transactions:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                return

            print("Распечатываю итоговый список транзакций...")
            print(f"Всего банковских операций в выборке: {len(transactions)}")
            for transaction in transactions:
                description = transaction.get("description")
                if description == "Открытие вклада":
                    from_ = description
                else:
                    from_ = mask_card(transaction.get("from"))

                to_ = mask_card(transaction.get("to"))
                date = mask_account(transaction.get("date"))

                amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["name"]

                if description == "Открытие вклада":
                    print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
                else:
                    print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")

        if __name__ == "__main__":
            main()

