#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 911.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.9}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'название сладости':
    [
         {'shop': 'название магазина', 'price': 99.99},
    ]
}
# TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)

sweets2 = {
    'печенье':
        [
            {'shop': 'ашан', 'price': 10.99},
            {'shop': 'пятерочка', 'price': 9.99},
            {'shop': 'магнит', 'price': 911.99},
        ],
    'конфеты':
        [
            {'shop': 'ашан', 'price': 34.99},
            {'shop': 'пятерочка', 'price': 32.99},
            {'shop': 'магнит', 'price': 30.99},
        ],
    'карамель':
        [
            {'shop': 'ашан', 'price': 45.99},
            {'shop': 'пятерочка', 'price': 46.99},
            {'shop': 'магнит', 'price': 41.99},
        ],
    'пирожное':
        [
            {'shop': 'ашан', 'price': 67.99},
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.9},
        ],
    'мороженное':
        [
            {'shop': 'ашан', 'price': 67.99},
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.9},
        ],
}
# TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
# Указать надо только по 2 магазина с минимальными ценами
sweets3 = {
    'печенье':
        [
            {'shop': 'ашан', 'price': 10.99},
            {'shop': 'пятерочка', 'price': 9.99},
        ],
    'конфеты':
        [
            {'shop': 'пятерочка', 'price': 32.99},
            {'shop': 'магнит', 'price': 30.99},
        ],
    'карамель':
        [
            {'shop': 'ашан', 'price': 45.99},
            {'shop': 'магнит', 'price': 41.99},
        ],
    'пирожное':
        [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.9},
        ],
    'мороженное':
        [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.9},
        ],
}
pprint(sweets2)
pprint(sweets3)
