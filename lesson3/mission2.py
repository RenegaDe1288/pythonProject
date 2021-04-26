qartal_1 = int(input('Введите доход за первый квартал: '))
qartal_2 = int(input('Введите доход за второй квартал: '))
qartal_3 = int(input('Введите доход за третий квартал: '))
qartal_4 = int(input('Введите доход за четвертый квартал: '))

half_year_1 = qartal_1 + qartal_2
half_year_2 = qartal_3 + qartal_4

dinamics = half_year_1/half_year_2

print(dinamics)
