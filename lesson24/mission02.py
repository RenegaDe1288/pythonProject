class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 60


class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = False


monitor_1 = Monitor()
monitor_2 = Monitor()
monitor_2.freq = 144
monitor_3 = Monitor()
monitor_3.freq = 70
monitor_4 = Monitor()
print(monitor_1.freq)
print(monitor_2.freq)
print(monitor_3.freq)
print(monitor_4.freq)

headphones_1 = Headphones()
headphones_2 = Headphones()
headphones_2.micro = True
headphones_3 = Headphones()
headphones_3.micro = True
print(headphones_1.micro)
print(headphones_2.micro)
print(headphones_3.micro)

Monitor.freq = 1000
Headphones.micro = 'UUUUU'
print(monitor_1.freq)
print(monitor_2.freq)
print(monitor_3.freq)
print(monitor_4.freq)
print(headphones_1.micro)
print(headphones_2.micro)
print(headphones_3.micro)