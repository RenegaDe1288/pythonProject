number = int(input('Введите четырехзначное число : '))
part_1 = number // 1000
part_2 = (number // 100) % 10
part_3 = (number // 10) % 10
part_4 = number % 10
print(part_1, part_2, part_3, part_4, sep='\n')