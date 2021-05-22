violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

n = 3

def count(songs, x):
    while True:
        print('Введите песню: {} '.format(x+1), end='')
        i = input()
        if i in violator_songs:
            return violator_songs[i]



total = round(sum([count(violator_songs,x) for x in range(n) ]), 2)
print('Общее время звучания песен:', total)
