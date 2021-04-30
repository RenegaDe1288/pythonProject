import random
number = random.randint(7, 120)

print('Икс равен', number)

dev = 1
dev_2 = 1
all_2 = 0
all = 0
for num in range(1, 7):
    tool_1 = number - (2 ** num - 1)
    tool_2 = number - (2 ** num)
    if tool_1 == 0:
        break
    if tool_2 == 0:
        break
    else:
        all = dev * tool_1
        dev = tool_1 * dev
        all_2 = dev_2 * tool_2
        dev_2 = tool_2 * dev_2
if all != 0 and all_2 != 0:
    print('Ответ == ', all / all_2)
