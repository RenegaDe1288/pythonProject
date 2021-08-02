class Point:

    def __init__(self, x=0, y=0):
        self.set_xcoordinates(x)
        self.set_ycoordinates(y)

    def __str__(self):
        try:
            return 'Координата х: {} \nкоордината у: {} '.format(self.__x, self.__y)
        except:
            Exception

    def get_xcoordinates(self):
        return 'Координата х: {}  '.format(self.__x)

    def get_ycoordinates(self):
        try:
            return 'Координата y: {} '.format((self.__y))
        except:
            Exception

    def set_xcoordinates(self, x):
        if isinstance(x, int):
            self.__x = x
        else:
            print('Не является числом')

    def set_ycoordinates(self, y):
        try:
            if isinstance(y, int):
                self.__y = y
            else:
                print('Не является числом')
                raise Exception('Ошибка Ввода')
        except:
            Exception


point_1 = Point(2, 'fdf')
print(point_1.get_xcoordinates())
print(point_1.get_ycoordinates())

print(point_1.__str__())
point_1.set_xcoordinates(3)
print(point_1.__str__())
point_1.set_ycoordinates(45)
print(point_1.__str__())
