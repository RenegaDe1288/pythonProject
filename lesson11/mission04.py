while True:
    chat = int(input('Введите количество чатлов: '))
    cr = 2200
    ship = round(chat/(cr/2), 2)
    print('Это ', round(chat/cr,2), 'CR' )
    print('За ', chat,' чатлов Вы можете куить ', int(ship), 'корабля')