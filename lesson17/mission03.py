def count():
    price = float(input('Введите цену: '))
    return round(price, 2)


def increase(price, percent):
    new_price = price * (1 + percent / 100)
    return new_price


price_list = [count() for num in range(5)]
increase_1 = int(input('Введите процент подорожания за первый год: '))
increase_2 = int(input('Введите процент подорожания за второй год: '))

new_price_list = [increase(num, increase_1) for num in price_list]
new_price_list2 = [increase(num, increase_2) for num in new_price_list]

print('Сумма цен за каждый год: ', round(sum(price_list), 2), round(sum(new_price_list), 2),
      round(sum(new_price_list2), 2))
