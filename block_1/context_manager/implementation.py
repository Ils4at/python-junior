class ContextManager:
    def __init__(self, file, method, encoding='utf-8'):
        self.file = open(file, method, encoding=encoding)
        self.method = method

    def __enter__(self):
        if self.method == "r":
            print(f"Количество строк в файле = {len(self.file.readlines())}")
            self.file.seek(0)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

# Запись в файл информацию
# with ContextManager('test.txt', 'w') as f:
#     f.write("""Тип, значение и обратная трассировка ошибки передается в метод __exit__
# Обработка исключения передается методу __exit__
# Тип, значение и обратная трассировка ошибки передается в метод __exit__
# Обработка исключения передается методу __exit__
# Тип, значение и обратная трассировка ошибки передается в метод __exit__
# Обработка исключения передается методу __exit__""")


with ContextManager('test.txt', 'r') as f:
    result = f.read()
print(result)
