from abc import ABC


class Transport(ABC):
    def __init__(self, new, color, speed):
        self.name = new
        self.color = color
        self.speed = speed

    def drive(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new):
        self._color = new

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new):
        self._speed = new

    def move(self):
        print('Двигаюсь вперед')

    def sound(self):
        print('Мой Сигнал БИИИИИ')

    def __str__(self):
        return '\nМашина: {} {} {}'.format(self.name, self.color, self.speed)


class PlaySound:

    def play_sound(self):
        print('Я проигрываю музыку')


class Auto(Transport, PlaySound):

    def drive(self):
        print('Я могу двигаться по дороге')


class Boat(Transport, PlaySound):

    def drive(self):
        print('Я могу двигаться по воде')


class Amphibia(Transport, PlaySound):

    def drive(self):
        print('Я могу двигаться по дороге и по воде')


auto = Auto('Lincoln', 'black', 200)
boat = Boat('Buick', 'white', 180)
amphibia = Amphibia('Cadillac', 'blue', 50)
print(auto)
auto.play_sound()
auto.drive()
auto.sound()
auto.move()
print(boat)
boat.play_sound()
boat.drive()
boat.sound()
boat.move()
print(auto.name)
auto.name = 'dffdffdffdfdf'
print(auto.name)
auto.color = 'redddd'
print(auto.color)
