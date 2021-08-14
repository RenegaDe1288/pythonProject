from functools import reduce

from typing import List

sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"]

numbers = reduce(lambda x, y: x + y,
                 (map(lambda x: 1, [filter(lambda elem: elem == 'was', i.split()) for i in sentences])))


print(numbers)
