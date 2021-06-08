site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search(struct, key):
    if key in struct:
        return struct[key]
    for sub in struct.values():
        if isinstance(sub, dict):
            text = search(sub,key)
            if text:
                break
    else:
        text = None
    return text


key = input('Введите ключ: ')
value = search(site,key)
if value:
    print(value)
else:
    print('нет')

print()