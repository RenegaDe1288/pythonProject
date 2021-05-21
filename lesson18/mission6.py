text = 'aAAbbсaaaA'
text = [x for x in text]+list(' ')
string = ''
count = 1
for x in range(len(text)-1):
    if text[x] == text [x+1]:
        count += 1
    else:
        string += text[x] + str(count)
        count = 1
print(string)

