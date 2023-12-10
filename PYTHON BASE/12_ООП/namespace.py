"""Как обращаться к переменным класса внутри функции"""


class DepartmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    """тут играет пространство имен. внутри функции не видны переменные класса. Будут видны, если вынести их за класс - в глобальную область"""

    # def info(self):
    #     print(PYTHON_DEV, GO_DEV, REACT_DEV)

    """Другие способы как обращаться к переменным класса"""
    # def info(self):
    #     print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    #
    # def info2(self):
    #     print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)
    #
    # @property
    # def info_prop(self):
    #     print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    #
    # @classmethod
    # def info_class(cls):
    #     print('info_class')
    #     print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)
    #
    # @staticmethod
    # def info_static():
    #     print('info_static')
    #     print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    """Как изменить значение переменной внутри класса и сохранить это состояние"""

    def hiring_pyt_dev(self):
        self.PYTHON_DEV = self.PYTHON_DEV + 1

    def hiring_pyt_dev2(self):
        DepartmentIT.PYTHON_DEV = DepartmentIT.PYTHON_DEV + 1


w = DepartmentIT()
# w.info()  # 4 3 2
# w.info2()  # 4 3 2
# w.info_prop  # 4 3 2
# w.info_class()  # info_class  # 4 3 2
# w.info_static()  # info_static  # 4 3 2

print(w.PYTHON_DEV)  # 4 - начальное значение
w.hiring_pyt_dev()
print(w.PYTHON_DEV)  # 5 - изменили с помощью функции
print(DepartmentIT.PYTHON_DEV)  # 4 - переменная в классе не изменилась
print(w.__dict__)  # {'PYTHON_DEV': 5} - получается что новое значение создается не у класса, а у экземпляра
w.hiring_pyt_dev2()
print(DepartmentIT.PYTHON_DEV)  # 5 - чтобы поменять значение переменной внутри класса, нужно непосредственно обращаться к ней через класс
print(w.__dict__)  # {} - тут у экземпляра ничего не создается
