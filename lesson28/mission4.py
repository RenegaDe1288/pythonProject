class Date:

    def __init__(self, time: list):
        print('Объект {} создан'.format(time))
        self.day, self.month, self.year = time[0], time[1], time[2]

    def __str__(self) -> str:
        return 'День: {}, Месяц : {}, Год : {}'.format(self.day, self.month, self.year)

    @classmethod
    def from_string(cls, time: str):
        try:
            time = time.split('-')
            if len(time) == 3:
                if int(time[0]) in range(1, 32) and int(time[1]) in range(1, 13) and int(time[2]) in range(2000,
                                                                                                           2100):
                    return Date(time)
            else:
                print('Неверное количество аргументов: ', len(time), time)
        except Exception:
            print('неверный формат даты', time)

    @classmethod
    def is_date_valid(cls, time: str) -> bool:
        if cls.from_string(time):
            return True
        else:
            return False


date = Date.from_string('11-11-2011')
print(date)

print(Date.is_date_valid('10-12-2077'))

print(Date.is_date_valid('40-12-2077'))

print(Date.is_date_valid('11-40-12-2077'))
print(Date.is_date_valid('gdfgd-vv-vb'))
