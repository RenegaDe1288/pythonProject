string = 'Я! Есть. Грут?! Я, Грут и Есть.'
sign = [sym for sym in string if not sym.isalpha() and sym != ' ']
print('Количество знаков пунктуации:', len(sign))
print('Знаки пунктуации: ', set(sign))
