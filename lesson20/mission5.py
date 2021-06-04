family = {'Сидоров Никита': 35,

          'Сидорова Алина': 34,

          'Сидоров Павел': 10,

          'Петрова Алена': 10,

          'Тришина Оксана': 25
          }

surname = input('Введите фамилию для поиска: ').lower()

total_age = sum([age for name, age in family.items() if surname[:len(surname) - 1] in name.lower()])
print('Общий возраст семьи с фамилией: {} составляет: {} лет'.format(surname, total_age))
