def view(list):
    new_str = ''
    for i in list:
        new_str += i
    return new_str


def find(x):
    global al
    x = al[(al.index(x) + 3) % 32]
    return x


a = ord('а')
al = [chr(i) for i in range(a, a + 32)]

message = 'это питон'

code = [find(x) if x != ' ' else ' ' for x in message]

print(view(code))

