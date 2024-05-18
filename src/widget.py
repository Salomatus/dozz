from src.masks import mask_account, mask_card


def mask_account_card(number: str) -> str:
    """Функция принимает и маскирует номер счета и карты"""
    if len(number.split()[-1]) == 16:
        new_number = mask_card(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
        return result
    elif len(number.split()[-1]) == 20:
        new_number = mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
    return result


def get_new_data(old_data: str) -> str:
    """Функция принимает строку старой даты и форматирует её"""
    data_slise = old_data[0:10].split("-")
    return ".".join(data_slise[::-1])