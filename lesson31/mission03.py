import re
s = 'Even if they  F are djinns, I will get djinns that can outdjinn them.'

res = re.findall(r'\b[AEIOUaeuoi]\w*',s)
res2 = re.findall(r'\b[^, AEIOUaeuoi\.]\w*',s)

print(res)
print(res2)