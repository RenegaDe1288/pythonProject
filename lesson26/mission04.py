from sympy import *


class Primes:

    def __init__(self,num):
        self.num = num
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.num >= self.count:
            if isprime(self.count):
                return str(self.count) + ' '
            else:
                return ''
        else:
            raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end='')