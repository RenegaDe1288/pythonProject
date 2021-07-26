import random


class Parent:

    def __init__(self, name):
        self.name = name
        self.age = random.randint(30, 50)
        self.childrens = ['Alex', 'Mike', 'Mary']

    def info(self):
        print('Отец, Имя : {}, Возраст: {},  Дети: {}'.format(self.name, self.age, self.childrens))


class Child:

    def __init__(self, name):
        self.name = name
        self.age = random.randint(1, 16)
        self.status = random.choice(['Плохо', 'Удовлитворительно', 'Хорошо'])
        self.hunger = random.choice(['Голоден', 'Хочет есть', 'Сыт'])

    def ch_info(self):
        print('Ребенок, Имя : {}, Возраст: {},  Состояние: {}, Голод: {}\n'.format(self.name, self.age, self.status,
                                                                                   self.hunger))

    def feed(self):
        print(self.name)
        if self.hunger != 'Сыт':
            answer = int(input('Хотите покормить ребенка? 1/2: '))
            if answer == 1:
                self.hunger = 'Сыт'
                print('Теперь {}  {}'.format(self.name, self.hunger))

    def play(self):
        if self.status != 'Хорошо':
            answer = int(input('Хотите поиграть с ребенком? 1/2: '))
            if answer == 1:
                self.status = 'Хорошо'
                print('Теперь {}  чувствует себя {}'.format(self.name, self.status))


father = Parent('John')
father.info()
print()
childrens = [Child(child) for child in father.childrens]
for child in childrens:
    child.ch_info()
    child.feed()
    child.play()
    child.ch_info()
