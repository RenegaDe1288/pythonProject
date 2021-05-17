goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

new_fruit = input("Введите новый фрукт: ")
new_price = int(input('Введите новую цену: '))
goods.append([new_fruit,new_price])

print(goods)

for num in range(0, len(goods)):
    goods[num][1] = round((goods[num][1]*1.08), 1)

print('Новые цена на фрукты: ', goods)