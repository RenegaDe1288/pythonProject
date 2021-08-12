import math


class Triangle:

    def __init__(self, length: (int, float), height: (int, float)):
        self._len = length
        self._hen = height

    def square(self) -> (int, float):
        square = self._len * self._hen / 2
        return square

    def triangle_perimeter(self) -> (int, float):
        c = round(math.sqrt(pow(self._len / 2, 2) + pow(self._hen, 2)), 2)
        perimeter_tri = c * 2 + self._len
        return perimeter_tri

    def __str__(self):
        print('Площаль треугольника: {} '.format(self.square()))

    @property
    def len(self) -> (int, float):
        return self._len

    @property
    def hen(self) -> (int, float):
        return self._hen

    @len.setter
    def len(self, new: (int, float)):
        self._len = new

    @hen.setter
    def hen(self, new: (int, float)):
        self._hen = new


class Square:

    def __init__(self, length: (int, float)):
        self._len = length

    def square(self):
        square = pow(self._len, 2)
        return square

    def square_perimeter(self) -> (int, float):
        perimeter = self._len * 4
        return perimeter

    @property
    def len(self) -> (int, float):
        return self._len

    @len.setter
    def len(self, new: (int, float)):
        self._len = new


class Cube:
    def __init__(self, length: (int, float)):
        self.cube = [Square(length) for _ in range(6)]

    def count_square(self) -> str:
        all_square = sum(i.square() for i in self.cube)
        return 'Общая площадь поверхности куба:  {}'.format(all_square)

    def count_perimeter(self) -> str:
        all_perimeter = sum(i.square_perimeter() for i in self.cube)
        return 'Общий периметр строн куба:  {}'.format(all_perimeter)


class Pyramid:
    def __init__(self, length: (int, float), height: (int, float)):
        self.pyramid = [Triangle(length, height) for _ in range(4)] + [Square(length)]

    def count_square(self) -> str:
        all_square = sum(i.square() for i in self.pyramid)
        return 'Общая площадь поверхности пирамиды:  {}'.format(all_square)


cube = Cube(3)
print(cube.count_square())
print((cube.count_perimeter()))
pyr = Pyramid(3, 5)
print(pyr.count_square())
