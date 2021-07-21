import random


class Toyota:
    color = 'blue'
    price = 1000000
    speed = 200
    current_speed = 0


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()
car_1.current_speed = random.randint(0, 200)
car_2.current_speed = random.randint(0, 200)
car_3.current_speed = random.randint(0, 200)
print(car_1.current_speed)
print(car_2.current_speed)
print(car_3.current_speed)
