alp = []
for i in range(97, 123):
    alp.append(chr(i))


file1 = open('text.txt', 'r')
text1 = file1.read().split('\n\n')
file = open('cipher_text.txt', 'w')

n = 1
for word in text1:
    new_str = ''
    for sym in word:
        new_str += alp[alp.index(sym.lower())+n]
    n += 1
    file.write(new_str + '\n')
    print(new_str)

file1.close()
file.close()


