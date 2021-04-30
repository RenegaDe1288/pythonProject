awake_time = int(input('Введите когда Саша проснулся: '))
total_calories = 0
count = 0
water = 0
for hour in range(awake_time, 23, 3):
    print('Час :', hour)
    calories = int(input('Введите сколько калорий получил Саша: '))
    total_calories += calories
    count += 3
    water += 1
    print(' Саша накопил калорий: ', total_calories)
    print('Саша выил длитров воды: ', water)
print()
print(' Саша пошел спать  в 23 -00')
print(' Саша получил ', total_calories, 'калорий за ', 23 - awake_time, ' часов')
print('Саша выил длитров воды: ', water)

