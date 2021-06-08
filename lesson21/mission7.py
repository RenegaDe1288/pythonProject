def summa(args, total=0):
    list_1 = (args)
    for i in list_1:
        if isinstance(i, int):
            total += i
        else:
            total = summa(i, total)
    return total


list1 = [[1, 2, [3]], [1], 3, [[1, [1, 2], 2], 2]]
print('Сумма чисел в списке равна: ', summa(list1))

print('Сумма чисел из набора параметров равна: ', summa((1, 2, 3, 6, 4, 5),total=0))



