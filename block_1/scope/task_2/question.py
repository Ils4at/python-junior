"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
"""
Ответ
"Test message" один раз только выводится так как в первой функции не указан print, transmit_to_space выведет None 
пустоту.   
"""