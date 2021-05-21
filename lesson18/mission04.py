names = input('Введите список слов: ').split()
text = input('Введите текст: ').split()
count = [x for x in text if x in names]
print('Количество повторений слов:', len(count))
