def mask_card(number: str) -> str:
    """Функция принимает строку и возвращаем маскировку карты"""
    new_string = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string


def mask_account(acc_number: str) -> str:
    """Функция принимает строку и возвращаем маскировку счета"""
    new_string = f"** {acc_number[-4:]}"
    return new_string