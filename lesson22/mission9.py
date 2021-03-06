import zipfile

fantasy_zip = zipfile.ZipFile('voyna-i-mir.zip')
link = fantasy_zip.extract('voyna-i-mir.txt')
print(link)

fantasy_zip.close()

file_1 = open(link, 'r', encoding='utf-8')
text = file_1.read().split('\n')

my_list = [sym for line in text for sym in line if sym.isalpha()]

letters = set(my_list)
dict_letters = {}

dict_letters = {my_list.count(letter): letter for letter in letters if letter not in dict_letters}

file = open('analysis.txt', 'w', encoding='utf-8')

for key in sorted(dict_letters, reverse=True):
    file.write(dict_letters[key] + ' ' + str(key) + '\n')

file_1.close()
file.close()
