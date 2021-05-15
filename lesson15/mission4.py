cards = []
new_cards = []
total = int(input('Введите количество видеокарт: '))
for _ in range(total):
    cards.append(int(input('Введите модель видеокарты: ')))

max = 0
for i in range(len(cards)):
    if cards[i] > max:
        max = cards[i]
print(max)

for i in range(len(cards)):
    if cards[i] < max:
        new_cards.append(cards[i])

print('Старый список карт: ', cards)
print('Новый список карт:', new_cards)
