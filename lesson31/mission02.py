import re

string = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?'

new = re.findall(r'\\wwood\+\?,', string)
print(new)
