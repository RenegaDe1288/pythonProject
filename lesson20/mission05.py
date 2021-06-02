import random
import string


def create_dict(list):
    new_dict = {}
    for index, value in enumerate(list):
        new_dict[index] = value
    return new_dict


letters = string.ascii_lowercase
rand_list1 = [random.choice(letters) for _ in range(10)]
rand_list2 = [random.choice(letters) for _ in range(10)]
dict_1 = create_dict(rand_list1)
dict_2 = create_dict(rand_list2)

print(f'Первый список: {rand_list1} \nВторой список: {rand_list2}')
print()
print(f'Первый словарь: {dict_1} \nВторой словарь: {dict_2}')
