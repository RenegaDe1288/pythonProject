import os

folder = 'access'
file = 'admin.bat'

abs_path = os.path.abspath(os.path.join(folder, file))
print('Абсолютный путь: ', abs_path)
rev_path = os.path.join('Skillbox', folder, file)
print('Относительный путь: ', rev_path)
print()

folder = 'pythonProject'
abs_path = os.path.abspath(os.path.join('..', '..', folder))
print(abs_path)
list_files = os.listdir('E:\Games\Destroy All Humans!')
for i in sorted(list_files):
    print(os.path.join(abs_path, i))
    # if len(list(os.listdir(os.path.join('E:\Games\Destroy All Humans!', i))))>1:
    #     for y in sorted(os.listdir(os.path.join('E:\Games\Destroy All Humans!', i))):
    #         print(os.path.join(i, y))