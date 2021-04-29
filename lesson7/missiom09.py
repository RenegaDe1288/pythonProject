awake_time = int(input('Введите когда Саша проснулся: '))
total_calories = 0
count = 0
for hour in range(awake_time, 23):
    calories = int(input('Введите сколько калорий получил Саша: '))
    total_calories += calories
    count += 1
    if total_calories >= 2000:
        print('Саша объелся и уснул')
        break
    if hour > 22:
        print(' Саша уснул в 23 часа')
    print(' Саша накопил калорий: ', total_calories)
    print('Час :', hour + 1)
print(' Саша получил ', total_calories, 'калорий за ', count, ' часов')