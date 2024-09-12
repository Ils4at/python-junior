from block_1.common import MyException


class ClassFather:
    registered_list = []

    @staticmethod
    def register():
        raise MyException()

    @staticmethod
    def get_name():
        raise MyException()


class User1(ClassFather):
    _name = ' '

    @staticmethod
    def register():
        ClassFather.registered_list.append(1)

    @staticmethod
    def get_name():
        if 1 in ClassFather.registered_list:
            return User1._name
        else:
            raise MyException()


class User2(ClassFather):
    _name = ' '

    @staticmethod
    def register():
        ClassFather.registered_list.append(2)

    @staticmethod
    def get_name():
        if 2 in ClassFather.registered_list:
            return User2._name
        else:
            raise MyException()


