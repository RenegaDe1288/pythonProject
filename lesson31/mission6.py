import re
import requests

text = (requests.get('http://www.columbia.edu/~fdc/sample.html')).text
x = re.findall(r'>\w.{1,}\b</h3>',text)
new_list = [i[1:-5] for i in x]

print(new_list)

