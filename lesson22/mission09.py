def copy(file):
    text = open(file, 'r', encoding='utf-8')
    for line in text:
        if line != '\n':
            script_file.write(line)
    script_file.write('\n\n' + '*' * 40 + '\n\n')
    text.close()


script_file = open('script.txt', 'a', encoding='utf-8')

for name in ['code1.txt', 'code2.txt']:
    copy(name)

script_file.close()
