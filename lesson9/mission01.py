count = 0
for students in range(5):
    answer = input('Кто написал произведение Евгений Онегин?')
    if answer == 'Пушкин':
        print('Правильный ответ! Больше не спрашиваю.')
        break
    else:
        count += 1
print('Количество двоечников = ',count)

