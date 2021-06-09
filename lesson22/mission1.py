text = open('answer.txt', 'r')
summ = 0
for line in text:
    if line != '\n':
        summ += int(line.lstrip())
print(summ)
text.close()
text = open('answer.txt', 'a', encoding='utf-8')
text.write('\nСодержимое файла answer.txt: ' + str(summ))
text.close()
