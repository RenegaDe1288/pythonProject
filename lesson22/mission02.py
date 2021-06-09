import os
abs_path = os.path.join('E:\Games\Destroy All Humans!')
print(abs_path)
list_files = os.listdir(abs_path)
for i in sorted(list_files):
    print(os.path.join(abs_path, i))

print(list_files)
