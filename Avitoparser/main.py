from bs4 import BeautifulSoup
import requests
import fake_useragent
import csv
import re


def main(response):
    data = BeautifulSoup(response, 'lxml')
    list = data.find('div', class_='items-items-3wYLB')
    list_1 = list.find_all('div',
                           class_='iva-item-root-nz94Y photo-slider-slider-3yhPU iva-item-list-2ptz- iva-item-redesign-d-JOB iva-item-responsive-lFce_ items-item-onmtx items-listItem-19eWR js-catalog-item-enum')
    return list_1


def check(list_1):
    count = 1
    for i in list_1:
        title = i.find('h3',
                       class_='title-root-oH7yP iva-item-title-3VXN3 title-listRedesign-25ckv title-root_maxHeight-9l4AM text-text-1la7J text-size-s-2vtIX text-bold-3aqLF').text
        title = re.sub('[^A-Za-zА-яЁа-яе .,!?:%^&\\\*#@=+()0-9/\-\\n\\t]', '', title)
        print(count)
        print(title)
        link = 'https://www.avito.ru' + i.find('div', class_='iva-item-titleStep-3eaUg').find('a').get('href')
        print(link)

        try:
            pic_link = i.find('ul', class_='photo-slider-list-2cUOp').find('li').get('data-marker')[19:]
        except AttributeError:
            pic_link = 'нет фото'
        print(pic_link)

        try:
            price = i.find('span', class_="price-price-3MojW").text
            price = int(re.sub('[^0-9]','',price))
        except ValueError:
            price = 'Цена  не указана'
        print(price)

        try:
            params = i.find('div', class_="iva-item-text-3QSLd text-text-1la7J text-size-s-2vtIX").text
            params = re.sub('[^A-Za-zА-яЁа-яе .,!?:%^&\\\*#@=+()0-9/\-\\n\\t]', '', params)
        except AttributeError:
            params = 'None'
        print(params)

        try:
            description = i.find('div', class_="iva-item-text-3QSLd iva-item-description-3NklG text-text-1la7J text-size-s-2vtIX").text
            description= re.sub('[^A-Za-zА-яЁа-яе .,!?:%^&*#@=+()0-9/\-\\n\\t\\\]','',description)
        except AttributeError:
            description = 'Нет описания'


        try:
            adress = i.find('span', class_="geo-address-12Kaf text-text-1la7J text-size-s-2vtIX").text
        except AttributeError:
            adress = i.find('div', class_="geo-georeferences-2gY4s text-text-1la7J text-size-s-2vtIX").text

        print(adress)

        try:
            date = i.find('div', class_="date-text-1a2C1 text-text-1la7J text-size-s-2vtIX text-color-noaccent-DFQB-").text
        except AttributeError:
            date = ' нет даты'
        print(date)
        try:
            name = i.find('div', class_='styles-root-1Am3L text-text-1la7J text-size-s-2vtIX').find('a').get('title')
        except AttributeError:
            name = 'нет имени'
            print('exception')
        print(name)
        try:
            company = i.find('span',
                         class_='iva-item-text-3QSLd iva-item-textColor-gray44-mvRDc text-text-1la7J text-size-s-2vtIX').text
        except AttributeError:
            company= 'Нет компании'
        print(company)
        count += 1
        write(title, link, pic_link, price, params, description, adress, date, name, company)



def write(title, link, pic_link, price, params, description, adress, date, name, company):
    try:
        with open('parser.csv', 'a', encoding='cp1251', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([title, link, pic_link, price, params, description, adress, date, name, company])
    except UnicodeEncodeError:
        print('ERRROR')
        with open('parser.csv', 'a', encoding='cp1251', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([title, link, pic_link, price, params])


def load(link):
    n = 1

    with open('parser.csv', 'w', encoding='cp1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ['Название', 'Ссылка на объявление', 'Ссылка на фото', 'Цена', 'Параметры', 'Описание', 'Адрес', 'Дата', 'Имя',
             'Компания'])


    # link = 'https://www.avito.ru/rossiya/avtomobili?q=mitsubishi+galant+8'
    while True:
        new_link = f'{link}&p={str(n)}'
        print(new_link)

        user = fake_useragent.UserAgent().random
        headers = {'header': user}
        print(headers)

        response = requests.get(new_link, headers=headers).text
        response = main(response)
        if len(response)!=0:
            check(response)
            n += 1

        else:
            break

