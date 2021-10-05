import requests
from datetime import date
import time


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


def search(data):
    """Обработка запроса и создание списка найденных отелей"""
    current_date = str(date.today())
    future_date = current_date[0:8] + str(int(current_date[8:]) + 1)
    distance, price, command, hotels_num, id_town, num_photos = data['distance'], data['price'], data['command'], data[
        'hotels_num'], data['id_town'], data['num_photos']

    print('Расстояние', distance)
    print('Диапазон', price)
    print('Команда', command)
    print('Количество отелей', hotels_num)
    print('IDГорода', id_town)
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

    querystring = {"destinationId": id_town, "pageNumber": "1", "pageSize": str(hotels_num), "checkIn": current_date,
                   "checkOut": future_date, "adults1": "1", "priceMin": str(price[0]), "priceMax": str(price[1]),
                   "sortOrder": order, "locale": "ru_RU", "currency": "RUB"}

    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "cda01bc117msh591672a1cc06751p1e6290jsnae154ff80d0c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    results = {}
    print(data)

    # Проверка наличия результатов поиска. Если нет результатов возврат 'NO'
    try:
        hlist = data["data"]['body']['searchResults']['results']
    except KeyError:
        pass
        hlist = []
    if len(hlist) == 0:
        print(hlist)
        print('Недостаточно найденных отелей')
        return 'NO'

    # Создание словаря с данными о каЖдом найденном отеле
    for num, hotel in enumerate(hlist):
        print('ИЩУ отель №', num)
        if float(hotel.get("landmarks")[0].get("distance")[0]) < distance:
            results[num] = {'id_hotel': hotel.get('id'), 'hname': hotel.get('name'), 'raiting': hotel.get("starRating"),
                            'address': hotel.get("address").get("streetAddress"),
                            'dist': hotel.get("landmarks")[0].get("distance"),
                            'price': hotel.get("ratePlan").get('price').get("current")}

            if num_photos != 0:
                check_photos_api(results, num, hotel, num_photos)
            if len(results) == 0:
                return 'NO'

            # Запись  файл сохранения истории поиска
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(command + ' ' + time.asctime() + ' ')
        for value in results.values():
            print('Записываю фото')
            file.write(str(value['hname'] + ', '))
        file.write('\n')
    return results


def check_photos_api(results, num, hotel, num_photos):
    """ Получение фото отеля"""

    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
    querystring = {"id": hotel.get('id')}
    headers = {
        'x-rapidapi-key': "cda01bc117msh591672a1cc06751p1e6290jsnae154ff80d0c",
        'x-rapidapi-host': "hotels4.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    photos = response.json()
    results[num]['photos'] = []

    # Проверка наличия фото отеля
    try:
        photos_list = photos["hotelImages"]
        for photo in photos_list:
            if len(results[num]['photos']) < num_photos:
                photo = photo['baseUrl'][0:-11] + '.jpg'
                results[num]['photos'].append(photo)
            else:
                break
    except KeyError:
        print('Недостаточно фото')
    except TypeError:
        print('Сервер не доступен')
