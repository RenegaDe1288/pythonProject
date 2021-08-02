class DivisionError(Exception):

    def __init__(self, x, y, message="нельзя делить большее на меньшее"):
        self.x = x
        self.y = y
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)

    def __str__(self):
        return f'{self.x} -> {self.y} -> {self.message}'


with open('numbers.txt', 'r') as file:
    for line in file:
        line = line.split()
        x, y = int(line[0]), int(line[1])
        if x > y:
            print(x / y)
        else:
            raise DivisionError(x, y)
