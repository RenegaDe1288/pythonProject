
import requests
from bs4 import BeautifulSoup


def pars(link):
    link = 'https://www.avito.ru/' + link
    print(link)
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    all_title = soup.find('div', class_='gallery-img-frame js-gallery-img-frame').get('data-title').split(',')
    title_1 = all_title[0]
    price = (soup.find('span', class_='js-item-price').get('content'))
    adress = str(soup.find('div', class_='item-address'))
    c = 0
    adress_str = ''
    for i in adress:
        if i == '>' or i == '<':
            c += 1
        elif c == 6 and i != "\n":
            adress_str += i
    print('Адрес:', adress_str)
    print('Название объявления:', title_1)
    print('Цена товара:', price)
    print()


for i in range(1, 2):
    page = i
    link = f'https://www.avito.ru/podolsk/transport?p={page}&q=galant'

    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', class_='index-content-2lnSO')
    search_block = soup.find_all('div', class_='iva-item-slider-37uKh')
    count_pages = 0
    for i in search_block:
        i_link = i.find('a').get('href')
        pars(i_link)
        count_pages += 1

    print('Обнаружено {} сайтов'.format(count_pages))
