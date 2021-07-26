class Toyota:
    def info(self):
        print('Цвет машины: {} \nЦена машины: {} \nСкорость машины: {} \nТекущая скорость: {}'
              .format(self.color, self.price, self.speed, self.current_speed))

    def __init__(self, color='blue', price=1000000, speed=200, current_speed=0):
        self.color = color
        self.price = price
        self.speed = speed
        self.current_speed = current_speed

    def set_speed(self, new_speed):
        self.current_speed = new_speed


car_1 = Toyota()
car_1.info()
car_1.set_speed(100)
print(car_1.current_speed)

car_2 = Toyota('red', 2000000, 20000, 30)
car_2.info()
