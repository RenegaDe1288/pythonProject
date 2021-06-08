site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def show(data):
    if isinstance(data, dict):
        for key in data:
            if key == 'title':
                data[key] = 'Куплю/продам {} недорого'.format(tel)
            if key == 'h2':
                data[key] = 'У нас самая низкая цена на {}'.format(tel)
            else:
                show(data[key])
    return data



# бля я не втыкаю, как защитить от изменения ебучий словарь......
# он сука меняется сам....
n = 2
all_site = {}
for i in range(n):
    tel = input('Введите название телефона: ')
    all_site['Сайт для ' + tel] = show(site)
    for key, value in all_site.items():
        print(key, value)

