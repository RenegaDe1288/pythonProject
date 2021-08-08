from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, x, y, len, hen):
        self.x = x
        self.y = y
        self.len = len
        self.hen = hen

    @abstractmethod
    def move(self, x, y):
        self.x = x
        self.y = y
        print('Теперь координаты: {}'.format(self.x, self.y))

    def __str__(self):
        print('Данные: {} {} {} {}'.format(self.x, self.y, self.len, self.hen
                                           ))


class Size:

    def change(self, x, y):
        self.len = x
        self.hen = y
        print('Новый размер: {} и {}'.format(x, y))


class Rectangle(Figure, Size):

    def move(self, x, y):
        self.x = x
        self.y = y
        print('Теперь            координаты: {}'.format(self.x, self.y))


class Square(Figure, Size):

    def __init__(self, x, y, len):
        super().__init__(x, y, len, len)

    def move(self, x, y):
        super().move(x, y)


a = Rectangle(1, 1, 1, 1)
b = Square(2, 2, 2)
a.__str__()
a.change(2, 3)
a.__str__()
b.__str__()
b.change(4, 4)
b.__str__()
