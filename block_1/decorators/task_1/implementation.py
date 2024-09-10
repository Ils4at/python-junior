import time


def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(arg1):
        start_time = time.time()
        base = function(arg1)
        end_time = time.time() - start_time
        print('Время выполнения функции составляет: ', end_time)
        return base
    return wrapper


@time_execution
def factorial(n):  # функция для проверки
    fact = 1
    for number in range(2, n + 1):
        fact *= number
        time.sleep(2)  # даем не большую задержку, что бы проверить что декоратор верно считает
    return fact


print(factorial(2))
