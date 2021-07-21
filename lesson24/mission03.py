class Toyota:
    color = 'blue'
    price = 1000000
    speed = 200
    current_speed = 0

    def info(self):
        print('Цвет машины: {} \nЦена машины: {} \nСкорость машины: {} \nТекущая скорость: {}'
              .format(self.color, self.price, self.speed, self.current_speed))

    def set_speed(self, new_speed):
        self.current_speed = new_speed


car_1 = Toyota()
car_1.info()
car_1.set_speed(100)
print(car_1.current_speed)
