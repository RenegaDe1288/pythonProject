import os
path = 'E:\Games\Destroy All Humans!'
path_lost = path.split('\\')
print('Корень диска : ', path_lost[0]+'\\\\')

path = 'E:\Games\Destroy All Humans!'
print('Корень диска : ', path[0:3])


print(os.path.dirname(os.path.dirname(path)))

while True:
    if len(path) != 3:
        path = os.path.dirname(path)
    else:
        print(path)
        break

path = 'E:\Games\Destroy All Humans!'
print(os.path.split(path)[0])

print(os.path.splitdrive(path))