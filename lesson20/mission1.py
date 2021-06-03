students = {

    1: {

        'name': 'Bob',

        'surname': 'Vazovski',

        'age': 23,

        'interests': ['biology, swimming']

    },

    2: {

        'name': 'Rob',

        'surname': 'Stepanov',

        'age': 24,

        'interests': ['math', 'computer games', 'running']

    },

    3: {

        'name': 'Alexander',

        'surname': 'Krug',

        'age': 22,

        'interests': ['languages', 'health food']

    }

}


def analising(dict):
    interest = []
    length = 0
    for value in dict.values():
        interest += value['interests']
        length += len(value['name'])
    return interest, length


for _id, data in students.items():
    print('ID: {} - Возраст: {}'.format(_id, data['age']))


interests, name_length = analising(students)
print('Общая длина имен: {}, \nСписок интересов: {}'.format(name_length, ', '.join(interests)))



