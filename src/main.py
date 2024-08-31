import json
import logging
from pathlib import Path
from src.config import file_path
from src.utils import (reader_transaction_excel,
                       get_currency_rates,
                       get_expenses_cards,
                       top_transaction,
                       get_greeting,
                       get_stock_price
                       )
from src.views import main
from src.read_excel import read_excel


ROOT_PATH = Path(__file__).resolve().parent.parent

logger = logging.getLogger("utils.log")
file_handler = logging.FileHandler("main.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

def mains(date: str, file_path: str, stocks: list, currency: list):
    """Функция создающая JSON ответ для страницы главная"""

    logger = file_path.parent.joinpath("logs", "main.log")
    logger.info("Начало работы главной функции (main)")
    greeting = get_greeting()
    my_list_trans = read_excel(file_path)
    final_list = main(my_list_trans, date)
    cards = get_expenses_cards(final_list)
    top_trans = top_transaction(final_list)
    stocks_prices = get_stock_price(stocks)
    currency_r = get_currency_rates(currency)
    logger.info("Создание JSON ответа")
    date_json = json.dumps(
        {
            "greeting": greeting,
            "cards": cards,
            "top_transactions": top_trans,
            "currency_rates": currency_r,
            "stock_prices": stocks_prices,
        },
        indent=4,
        ensure_ascii=False,
    )
    logger.info("Завершение работы главной функции (main)")
    return date_json


def main_transactions():
    """Функция управления проектом"""
    print(
        """Добро пожаловать в раздел 'Сервис'
    Предлагаем ознакомиться с возможностями Инвест-копилки.
    Хотите знать, сколько денег Вы могли бы отложить в Инвест-копилку за месяц?"""
    )
    while True:
        es_no = input("Введите 'да' или 'нет': ").lower()
        if es_no == "да":
            # Читаем данные из excel-файла
            transactions = reader_transaction_excel(file_path)
            # Запрашиваем лимит округления
            while True:
                limit = int(
                    input(
                        "Выберите комфортную Вам сумму округления остатка для инвест-копилки."
                        "Введите число 10, 50 или 100: "
                    ))
                if limit == 10 or limit == 50 or limit == 100:
                    print(f"Выбрано округление до {limit} рублей")
                    break
                else:
                    print("Ошибка ввода")
                    continue
                    # Запрашиваем месяц
                while True:
                    month_choice = int(
                        input(f'Для расчета возьмём 2021 год. Введите порядковый номер месяца {range(1, 13)}: ')
                    )
                    if 0 < month_choice < 10:
                        month = "2021-0" + str(month_choice)
                        break
                    elif 9 < month_choice < 13:
                        month = "2021-" + str(month_choice)
                        break
                    else:
                        print("Ошибка. Введите число в диапазоне от 1 до 12.")
                        continue

                        def get_transactions_fizlicam(transactions, month, limit):
                            logger.info(f"Производим расчет сумм для инвест-копилки на {month}")
                            # создаем json-строку
                            data = {'total_investment': 'total_investment'}
                            json_data = json.dumps(data)
                            print(f"Json-ответ: {json_data}")
                            return json_data

                        if __name__ == "__main__":
                            get_transactions_fizlicam(transactions, month, limit)

                        while True:
                            es_no = input("Хотите продолжить? (да/нет): ")
                            if es_no == "да":
                                # выполните код для продолжения работы
                                continue
                            elif es_no == "нет":
                                print("Хорошо. До встречи!")
                                break
                            else:
                                print("Ошибка ввода")
                                continue

                if __name__ == "__main__":
                    main()
