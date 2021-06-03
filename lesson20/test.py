import webbrowser
from splinter import Browser
import pandas as pd
browser = Browser('chrome')
browser.visit('https://yandex.ru/search/?text=%D0%B0%D0%B2%D0%B8%D1%82%D0%BE&clid=1923020&lr=10747')

path ='/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/ul/li[2]/div/h2/a'
search_bar = browser.find_by_xpath(path)[0]
print(search_bar)


