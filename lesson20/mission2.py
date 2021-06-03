def is_prime(n):
    if n <= 2:
        return True
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def check(text):
    new_list = []
    try:
        if iter(text):
            new_list = [value for index, value in enumerate(text) if is_prime(index)]
    except TypeError:
            print('error')
    print(new_list)
    return new_list


text = input('Введите текст: ')
# text = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# new_list1 = [value for index, value in enumerate(text) if index % 2 == 0]
# print(new_list1)
new_list3 = check(text)
