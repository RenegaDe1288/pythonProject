import random


class Person:

    def __init__(self, name):
        self.age = random.randint(10, 40)
        self.name = name


persons = [Person(name) for name in ['n', 'm', 'o', 'd', 'z']]
print([i.age for i in persons])
sorted_persons = sorted(persons, key=lambda elem: elem.age)
print([i.age for i in sorted_persons])

sorted_persons = sorted(persons, key=lambda elem: elem.name)
print([i.name for i in sorted_persons])
