import random


class Point:

    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.count = count + 1


    def info(self):
        print('\nкоординаты точки: {} и {}'.format(self.x, self.y))
        print('количество точек: ', self.count)


point_1 = Point(random.randint(0, 20), random.randint(0, 20), 0)
point_1.info()
point_2 = Point(random.randint(0, 20), random.randint(0, 20), point_1.count)
point_2.info()
point_3 = Point(random.randint(0, 20), random.randint(0, 20), point_2.count)
point_3.info()
point_4 = Point(random.randint(0, 20), random.randint(0, 20), point_3.count)
point_4.info()

