dictoin = {}
x = 0
for num in range(6):
    order = input('Введите заказ: ').split()
    print(order)
    if order[0] in dictoin:
        for i in dictoin[order[0]]:
            if order[1] in i:
                dictoin[order[0]][dictoin[order[0]].index(i)][order[1]] += int(order[2])
                break
        else:
            dictoin[order[0]].append({order[1]: int(order[2])})
    else:
        dictoin[order[0]] = []
        dictoin[order[0]].append({order[1]: int(order[2])})
        x += 1
        print(dictoin)
for i in dictoin:
    print(i, dictoin[i])

