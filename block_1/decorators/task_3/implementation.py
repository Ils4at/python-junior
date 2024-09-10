def counter(function):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        return count

    return wrapper

    #raise NotImplementedError
