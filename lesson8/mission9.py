import random

number = random.randint(7, 9)

print('Икс равен', number)

dev = 1
dev_2 = 1
all_2 = 0
all = 0
for num in range(1, 7):
    tool_1 = number - (2 ** num - 1)
    if tool_1 == 0:
        print('В скобке', num, 'Числителя произведение равно 0.')
        all = 0
        break
    else:
        all = dev * tool_1
        dev = tool_1 * dev
        print()
        print('На шаге = ', num, ' +++++ вычисление равно', tool_1, '. перемножение ==', all)
if all != 0:
    for num in range(1, 7):
        tool_2 = number - (2 ** num)
        if tool_2 == 0:
            print('В скобке', num, 'Знаменателя произведение равно 0')
            print('На ноль делить нельзя. попробуйте другое значение!')
            all_2 = 0
            break
        else:
            all_2 = dev_2 * tool_2
            dev_2 = tool_2 * dev_2
            print()
            print('На шаге = ', num, ' ---- вычисление равно', tool_2, '. перемножение ==', all_2)
    print()
elif all == 0:
    print(' Ответ == 0')
if all != 0 and all_2!= 0:
    print('Числительное равно  == ', all)
    print("Знаменатель равен == ", all_2)
    if all!=0 and all_2!= 0:
        print('Ответ == ', all / all_2)
