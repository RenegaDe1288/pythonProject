import random


class Student:

    def __init__(self, name):
        self.name = name
        self.group = random.randint(1, 4)
        self.points = random.choices([1, 2, 3, 4, 5], k=5)
        self.average = sum(self.points) / 5

    def info(self, student):
        print('Студент: {}, группа: {}, оценки: {}, Средний балл: {}'
              .format(self.name, self.group, self.points, self.average))
        students.remove(student)


names_list = ['Abby', 'Sam', 'Ben', 'Cortny', 'Alice']
students = [Student(name) for name in names_list]
average_list = [student.average for student in students]
print('\nОтсортированный список: \n')

list = [student.info(student) for point in sorted(average_list) for student in students if point == student.average]
