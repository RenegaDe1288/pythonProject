#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =garden
# meadow_set =meadow
# TODO здесь ваш код
garden_set =set(garden)
meadow_set =set(meadow)

print(garden_set,meadow_set)

# выведите на консоль все виды цветов
# TODO здесь ваш код

all_set=garden_set|meadow_set
print(all_set)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код

every_set=garden_set&meadow_set
print(every_set)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код

gs_set=garden_set-meadow_set
print(gs_set)


# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код

sg_set=meadow_set-garden_set
print(sg_set)

