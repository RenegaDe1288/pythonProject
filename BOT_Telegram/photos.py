import requests
from datetime import date
import datetime
import time



c = time.asctime()
print(c)

current_date = str(date.today())
print(len(current_date))
future_date = current_date[0:8] + str(int(current_date[8:]) + 1)
print(len(future_date))
print(future_date)
