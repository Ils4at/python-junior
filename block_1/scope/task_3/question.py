"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)

"""
Ответ 
3 3 Так как nonlocal охватывает переменную из области видимости функции. Ближайшая область в нашем случае это функция 
print_msg"""