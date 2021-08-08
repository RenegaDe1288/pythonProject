import math


class MyMath:

    @classmethod
    def circle_len(cls, radius):
        len_1 = 2 * math.pi * radius
        return 'Длина окружности: ' + str(len_1)

    @classmethod
    def circle_sq(cls, radius):
        sq = math.pi * radius ** 2
        return 'Площадь круга: ' + str(sq)

    @classmethod
    def cube_volume(cls, line):
        vol = line ** 3
        return 'Объем куба: ' + str(vol)

    @classmethod
    def sphere_sq(cls, radius):
        sq = 4 * math.pi * radius ** 2
        return 'Площадь поверхности сферы: ' + str(sq)


res_1 = MyMath.circle_len(radius=5)

res_2 = MyMath.circle_sq(radius=6)

res_3 = MyMath.cube_volume(line=6)

res_4 = MyMath.sphere_sq(radius=6)

print(res_1)

print(res_2)

print(res_3)

print(res_4)
