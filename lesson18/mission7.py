
while True:
    ip = input('\nВведите ip: ')
    ip_list = ip.split('.')
    for num in ip_list:
        if ip.count('.') != 3:
            print('Адрес - это четыре числа, разделённые точками')
            break
        elif not num.isdigit():
            print(num, '- не целое число')
            break
        elif int(num) > 255:
            print('{} превышает 255'.format(num))
            break
    else:
        print('Верный айпи:', ip)
        break





