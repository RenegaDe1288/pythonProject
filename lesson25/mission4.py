import random


class Person:

    def __init__(self):
        self.__name = random.choice(['Mike', 'Anna', 'Nick', 'Lesa', 'Stan'])
        self.__surname = random.choice(['Anina', 'Smirnof', 'Petrov', 'Sechin'])
        self.__age = random.randint(20, 40)

    def __get__(self, price):
        return ('Имя : {} \tФамилия : {} \tВозраст : {} \tЗарплата : {}'.format(self.__name, self.__surname, self.__age,
                                                                                price))


class Employee(Person):

    def salary(self):
        pass


class Manager(Employee):

    def __init__(self):
        super().__init__()
        self.price = 13000

    def salary(self):
        print(super().__get__(self.price))
        return self.price


class Agent(Employee):
    def __init__(self):
        super().__init__()
        self.persent = 0.05 * random.randint(10000, 100000)
        self.price = 5000

    def salary(self):
        self.price = self.persent + self.price
        print(super().__get__(self.price))
        return self.price


class Worker(Employee):

    def __init__(self):
        super().__init__()
        self.hours = random.randint(50, 100)
        self.price = 100

    def salary(self):
        self.price = self.hours * self.price
        print(super().__get__(self.price))
        return self.price


managers = [Manager() for _ in range(3)]
agents = [Agent() for _ in range(3)]
workers = [Worker() for _ in range(3)]
all_persons = managers + agents + workers
all_salaries = [person.salary() for person in all_persons]
total_salary = sum(all_salaries)
print('Общая зарплата: ', round(total_salary, 2))
