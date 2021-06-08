site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': {1: 'Тут, наверное, какой-то блок',
                    'p': 'А вот здесь новый абзац'}
        }
    }
}


def search(data, key, d):
    if data.get(key):
        print('Значение ключа {} это: {}'.format(search_key, data[key]))
        print('Ключ : {} найден на глубине: {} '.format(search_key, d))
        return True
    else:
        for item in data.values():
            if isinstance(item, dict) and d != depth:
                if search(item, key, d + 1):
                    return True


search_key = 'p'
#Максимальная глубина
depth = 2
if search(site, search_key, 0) == None:
    print('Нет такого ключа на указанной глубине')
