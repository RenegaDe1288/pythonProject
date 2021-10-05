import requests
from datetime import date
import datetime


def check_town(town: str) -> tuple or bool:
    """Проверка города через рапидапи. ТакЖе проводится поиск и по словам с ошибками"""
    url = "https://hotels4.p.rapidapi.com/locations/search"
    querystring = {"query": str(town), "locale": "ru_RU"}
    headers = {
        'x-rapidapi-key': "cda01bc117msh591672a1cc06751p1e6290jsnae154ff80d0c",
        'x-rapidapi-host': "hotels4.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    res = response.json()
    try:
        town_id = res["suggestions"][0]['entities'][0]['destinationId']
        name_town = res["suggestions"][0]['entities'][0]['name']
        print('Название города: ', name_town)
        print('ID города: ', town_id)
        return town_id, name_town
    except IndexError:
        print('Город не найден')
        return False


def search(id_town, hotels_num, command, price, distance, num_photos):
    """Обработка запроса и создание списка найденных отелей"""
    sd = str(date.today())
    print('Расстояние', distance)
    print('Диапазон', price)
    print('Команда', command)
    print('Количество отелей', hotels_num)
    print('IDГород', id_town)
    print('Количесто фото: ', num_photos)

    if command == '/higher':
        order = "PRICE_HIGHEST_FIRST"
    elif command == '/lower':
        order = "PRICE"
    else:
        order = 'DISTANCE_FROM_LANDMARK'

    if len(price) == 0:
        price = [0, 1000000]

    url = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {"destinationId": id_town, "pageNumber": "1", "pageSize": str(hotels_num), "checkIn": sd,
                   "checkOut": "2020-08-19", "adults1": "1", "priceMin": str(price[0]), "priceMax": str(price[1]),
                   "sortOrder": order, "locale": "ru_RU", "currency": "RUB"}

    headers = {
        'x-rapidapi-key': "cda01bc117msh591672a1cc06751p1e6290jsnae154ff80d0c",
        'x-rapidapi-host': "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    results = {}

    # Проверка наличия результатов поиска. Если нет результатов возврат 'NO'
    try:
        hlist = data["data"]['body']['searchResults']['results']
    except KeyError:
        print('Недостаточно найденных отелей')
        return 'NO'
    print(type(data))

    print(hlist)

    # Создание словаря с данными о каЖдом найденном отеле
    for x, i in enumerate(hlist):
        print('ИЩУ отель №', x)
        if float(i.get("landmarks")[0].get("distance")[0]) < distance:
            results[x] = {'id_hotel': i.get('id'), 'hname': i.get('name'), 'raiting': i.get("starRating"),
                          'address': i.get("address").get("streetAddress"),
                          'dist': i.get("landmarks")[0].get("distance"),
                          'price': i.get("ratePlan").get('price').get("current")}

            if num_photos != 0:
                check_photos_api(results, x,i,num_photos)
    if len(results) == 0:
        return 'NO'

    # Запись  файл сохранения истории поиска
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(command + ' ' + str(datetime.time) + ' ')
        for i, k in results.items():
            print(i, k)
            file.write(str(k['hname'] + ', '))
        file.write('\n')
    return results


def check_photos_api(results,x,i,num_photos):
    """ Получение фото отеля"""

    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
    querystring = {"id": i.get('id')}
    headers = {
        'x-rapidapi-key': "cda01bc117msh591672a1cc06751p1e6290jsnae154ff80d0c",
        'x-rapidapi-host': "hotels4.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    photos = response.json()
    results[x]['photos'] = []

    # Проверка наличия фото отеля
    try:
        photos_list = photos["hotelImages"]
        for y in photos_list:
            if len(results[x]['photos']) < num_photos:
                y = y['baseUrl'][0:-11] + '.jpg'
                results[x]['photos'].append(y)
            else:
                break
    except KeyError:
        print('Недостаточно фото')
    except TypeError:
        print('Сервер не доступен')



