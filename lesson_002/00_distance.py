#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей рас+стояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
# TODO здесь заполнение словаря
moscow_london = ((sites['Moscow'][0]-sites['London'][0])**2+(sites['Moscow'][1]-sites['London'][1])**2)**.5
moscow_paris = ((sites['Moscow'][0]-sites['Paris'][0])**2+(sites['Moscow'][1]-sites['Paris'][1])**2)**.5
paris_london = ((sites['Paris'][0]-sites['London'][0])**2+(sites['Paris'][1]-sites['London'][1])**2)**.5
distances = {
    'Москва': {'Лондон': moscow_london, 'Париж': moscow_paris},
    'Лондон': {'Париж': paris_london, 'Москва': moscow_london},
    'Париж': {'Лондон': paris_london, 'Москва': moscow_paris},
}

pprint(distances)
print('от Москвы до Лондона:', moscow_london)
