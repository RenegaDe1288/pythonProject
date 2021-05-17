n = int(input('Введите количество участников: '))
k = int(input('Введите сколько участников в команеде: '))
my_list = []
player = 1
if n%k != 0:
    print('Участики ни могут быть поровну разделены на команды. ')
else:
    for team in range(int(n/k)):
        my_list.append(list(range(player, player+k)))
        player += k
print(my_list)