text = open('zen.txt', 'r')
text1 = text.read().split('\n')
for line in text1[::-1]:
    print(line)

text.close()

