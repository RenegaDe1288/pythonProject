file = open('people.txt','r')

my_list = file.readlines()
print(my_list)
for pos, string in enumerate(my_list):
    string = string.removesuffix('\n')
    if string.isalpha():
        print('Слово в {} строке  состоит из букв'.format(pos+1))
    else:
        raise BaseException('В слове {} в строке {} есть числа'.format(string,pos+1))

file.close()