import json
import os
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
