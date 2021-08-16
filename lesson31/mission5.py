
from itertools import *

list_num = [str(i) for i in range(10)]
variations = product(list_num, repeat=4)
for i in variations:
    print(''.join(i))

