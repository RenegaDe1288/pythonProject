import random


class Circle:

    def __init__(self):
        self.x = random.randint(0, 5)
        self.y = random.randint(0, 5)
        self.radius = random.randint(1, 5)

    def info(self):
        print('Координаты х = {}, координаты у = {}, радиус = {}'.format(self.x, self.y, self.radius))

    def calculation(self):
        square = (self.radius ** 2) * 3.14
        perimeter = 2 * 3.14 * self.radius
        print('Площадь круга = {} , Периметр круга = {} '.format(square, float(perimeter)))

    def increase(self):
        x = random.randint(2, 3)
        self.radius = self.radius * x
        print(' Круг увеличен в {} раза'.format(x))

    def do_intersect(self, c_2):
        dist = ((self.x - c_2.x) ** 2 + (self.y - c_2.y) ** 2) ** 0.5
        if abs(self.radius - c_2.radius) <= dist <= self.radius + c_2.radius:
            return True


circles = [Circle() for _ in range(3)]

for circle_1 in circles:
    for circle_2 in circles:
        if circle_1.do_intersect(circle_2):
            print('Круги пересекаются')
        else:
            print('Круги не пересекаются')
print()
for circle in circles:
    circle.info()
    circle.calculation()
    circle.increase()
    circle.info()
    print()
