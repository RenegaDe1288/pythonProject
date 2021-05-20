def view(list):
    for i in list:
        print(i, end='')
    print()


def find(x):
    global al
    if al.index(x) < 29:
        x = al[al.index(x) + 3]
    else:
        x = al[abs(len(al) - al.index(x) - 3)]
    return x


a = ord('а')
al = [chr(i) for i in range(a, a + 32)]

message = 'это питон'
code = list(message)

code = [find(x) if x != ' ' else ' ' for x in code]

view(code)

# code = [al[al.index(x) + 3]  if x != ' '  else ' ' for x in code]
#
# view(code)
