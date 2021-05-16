new_pacs = []
total = int(input('Введите количество пакетов:'))
bad = 0
for i_pack in range(total):
    packs = []
    for num in range(4):
        print('Введите бит номер ', num + 1, 'от пакета ', i_pack + 1, end=' ')
        bit = int(input())
        packs.append(bit)
    if packs.count(-1) < 2:
        print('Пакет добавлен')
        new_pacs.extend(packs)
    else:
        bad += 1
        print('В пакете много ошибок. Пакет', i_pack + 1, ' потерян.')
    print('Новый пакет: ', new_pacs)
print('Количество потерянных пакетов = ',bad)
print('Количество ошибок в сообщении = ', new_pacs.count(-1))
