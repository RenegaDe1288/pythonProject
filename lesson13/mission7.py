amp = float(input('Введите начальную амплитуду: '))
stop = float(input('Введите амплитуду остановки: '))
count = 1
if amp > stop:
    while amp > stop:
        count += 1
        amp = amp - amp * 0.086
    print('Маятник считается остановившимся через', count, ' колебаний')
else:
    print('Маятник остановился')
