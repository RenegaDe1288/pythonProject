import os
def size(path):
    total = 0
    num = 0
    folder = 0
    for i in os.listdir(path):
        link = os.path.join(path, i)
        if os.path.isdir(link):
            data = size(link)
            total += data[0]
            num += data[1]
            folder += data[2] + 1
        else:
            total += os.path.getsize(link)
            num += 1
    return total, num, folder



path1 = 'E:\\Games'
total, sum_files, sum_dir = size(path1)
directory = os.path.split(path1)[1]

print('Общий размер папки {} : {} Мб '.format(directory, round(total/1024)/1024, 2))
print('Общее количество файлов в папке {} :  {} '.format(directory, sum_files))
print('Общее количество папок в папке  {} : {} '.format(directory, sum_dir))

