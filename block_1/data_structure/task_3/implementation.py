import copy


def copy_dict(origin_dict: dict) -> dict:
    """
    Функция возвращает копию словаря.
    """
    copy_dicts = copy.deepcopy(origin_dict)
    return copy_dicts