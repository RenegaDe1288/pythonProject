import random

begin_nun = random.randint(2, 3)
end_num = random.randint(9,20)
print('Список от', begin_nun, 'до ', end_num)
summ = 0
count = 0
for num in range(begin_nun,end_num + 1):
    if num % 3 == 0:
        summ += num
        count += 1
        print('Число кратное 3 --', num)
print(summ)
print('Среднее арифметиское', count, ' равно ', summ/count)
