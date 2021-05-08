exi = 0


def corridor():
    x = int(input('Вы в коридоре. Куда идем? \n1 — в спальню, \n2 — в ванну, \n3 — на кухню,\n4 — в дверь\n'))
    if x == 1:
        sleep()
    elif x == 2:
        wanna()
    elif x == 3:
        kitchen()
    elif x == 4:
        print('Вы свалили из дурдома')
        return
    else:
        corridor()


def wanna():
    x = int(input('Вы в ванне. Куда идем? \n1 - в спальню, \n2 - в коридор\n'))
    if x == 1:
        sleep()
    elif x == 2:
        corridor()
    else:
        wanna()

def kitchen():
    x = int(input('Вы в кухне. Куда идем? \n1 - в коридор, \n2 - в окно\n'))
    if x == 1:
        corridor()
    elif x == 2:
        print('Вы грохнулись с 17 этажа и разбились')
        return
    else:
        kitchen()

def sleep():
    x = int(input('Вы в спальне. Куда идем? \n1 - в ванну, \n2 - в коридор\n'))
    if x == 1:
        wanna()
    elif x == 2:
        corridor()
    else:
        sleep()

corridor()
