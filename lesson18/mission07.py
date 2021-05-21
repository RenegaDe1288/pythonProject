
a = ord('а')
al = [chr(i) for i in range(a, a + 32)]

message = 'Это пиТон'

code = ''.join([al[(al.index(x.lower()) + 3) % 32].lower()
        if x != ' ' else ' '
        for x in message])

print(code)
