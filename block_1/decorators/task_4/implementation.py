from block_1.common import MyException, specific_func
import time


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def decorator(function):

        def wrapper():
            nonlocal times
            for i in range(1, times + 1):
                try:
                    result = function()
                    return result
                except AssertionError:
                    if i == times:
                        raise MyException(Exception)
                i += 1
                time.sleep(delay)

        return wrapper
    return decorator

    # raise NotImplementedError