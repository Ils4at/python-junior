class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """
    def __init__(self, *args, **kwargs):
        self.list_tuple = args

    def __getitem__(self, i):
        return self.list_tuple[i]

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        count = 0
        for item in self.list_tuple:
            if item == value:
                count += 1
            else:
                pass
        return count

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        count = 0
        for item in self.list_tuple:
            if item == value:
                return count
            count += 1
        raise ValueError



