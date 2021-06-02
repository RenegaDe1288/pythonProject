data = {

    (5000, 123456): ('Иванов', 'Василий'),

    (6000, 111111): ('Иванов', 'Петр'),

    (7000, 222222): ('Медведев', 'Алексей'),

    (8000, 333333): ('Алексеев', 'Георгий'),

    (9000, 444444): ('Георгиева', 'Мария')

}

while True:
    serial_list = input('Введите номер паспорта: ').split(',')
    serial = tuple([int(i) for i in serial_list])
    print(serial)
    if serial in data:
        print(data[serial])
