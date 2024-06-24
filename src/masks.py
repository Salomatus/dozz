import os

from typing import Any

from src.logger import setup_logger


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_1)


def mask_card(number: str) -> str:
    """Функция принимает строку и возвращаем маскировку карты"""

    logger.info(f'Задаём формат маски для номера банковской карты {number}')

    new_string = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string


def mask_account(numbered: str) -> Any:
    """Функция принимает строку и возвращаем маскировку счета"""

    logger.info(f'Проверяем правильность написания {numbered}')
    if len(str(numbered)) != 20:
        logger.error(f'Ошибка. Проверьте номер счёта, он должен содержать 20 цифр')
        raise ValueError(f'Проверьте номер счёта, он должен содержать 20 цифр')
    else:
        logger.info(f'Задаём формат маски для номера банковского счета {numbered}')
        new_string = f"** {numbered[-4:]}"
    return new_string
