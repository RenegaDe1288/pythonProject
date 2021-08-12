import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.time()
    print(start)
    yield
    print(time.time())
    print('Время выполнения = ', time.time() - start)
    print('Конец функции')


with timer() as next:
    print('Первая часть')
    s = 365464564**22332 *1644649 * 4343424324 * 3242424 * 8768585895857949749747949*45353453535*5345535435345*43543534535
