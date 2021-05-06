eur  = float(input('Введите сумму в евро: '))

rur = round((eur*1.25 * 60.87),2)
print('В рублях =  ', int( rur), 'рублей', rur*100%100, 'коп')

