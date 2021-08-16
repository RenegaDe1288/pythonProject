import re

string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

print(re.match(r'wo', string))
print((re.search(r'wo', string)).start())
print((re.search(r'wo', string)).group(0))
print((re.search(r'wo', string)).end())
print((re.findall(r'wo', string)))
new = re.sub(r'wo', 'Замена', string)
print(new)
