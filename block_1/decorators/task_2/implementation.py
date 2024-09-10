from block_1.common import MyException
import functools


@functools.cache
def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(arg):
        if type(arg) == int and arg >= 0:
            result = function(arg)
            return result
        else:
            raise MyException(Exception)

    return wrapper
    # raise NotImplementedError

