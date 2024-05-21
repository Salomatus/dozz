def mask_card(number: str) -> str:
    """Функция принимает строку и возвращаем маскировку карты"""
    new_string = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string


def mask_account(numbered: str) -> str:
    """Функция принимает строку и возвращаем маскировку счета"""
    new_string = f"** {numbered[-4:]}"
    return new_string
