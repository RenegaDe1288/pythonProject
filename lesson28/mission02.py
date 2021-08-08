from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    @abstractmethod
    def drive(self):
        pass

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
