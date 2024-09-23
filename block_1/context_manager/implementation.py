class ContextManager:
    def __init__(self, file, method, encoding='utf-8'):
        self.file = open(file, method, encoding=encoding)
        self.f = open(file, method, encoding=encoding)

    def __enter__(self):
        print(f"Количество строк в файле = {len(self.file.readlines())}")
        self.file.seek(0)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()


with ContextManager('test.txt', 'r') as f:
    result = f.read()
print(result)
