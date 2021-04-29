import random

all_cards = random.randint(4, 6)
print('всего карт ', all_cards)
total_summ = 0
summ = 0

for card in range(1, all_cards + 1):
    total_summ += card
    if card < all_cards:
        card = int(input('Введите номер оставшейся карты: '))
        summ += card
lost_card = total_summ - summ
print('Потерявшаяся карта =', lost_card)
