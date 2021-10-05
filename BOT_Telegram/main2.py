import telebot
from telebot import types
from r1 import search, check_town
import re

bot = telebot.TeleBot('1966024506:AAHwTlK-WOoE-YrNTwMJL-V-60thb0bzpX0')

data = {'town': '', 'price': [], 'command': '/lower', 'hotels_num': 0, 'distance': 20, 'id_town': '', 'num_photos': 0}


class User:

    """User class"""

    def __init__(self, message) -> None:
        self.message = message

    def __str__(self) -> str:
        return f'{self.message.chat.id}: {self.message.chat.first_name} {self.message.chat.last_name}'





@bot.message_handler(commands=['start'])
def send_welcome(message):
    """ Вывод приветственного сообщения и открытие панели команд"""
    bot.send_message(message.from_user.id,
                     'ПРИВЕТ ! Я ПОМОГУ ТЕБЕ ВЫБРАТЬ ОТЕЛЬ!\n/lower - Отели по низким ценам '
                     '\n/higher - Отели по высоким ценам \n/price - Выбрать диапазон цен для отелей'
                     '\n/history - История запросов')


@bot.message_handler(commands=['lower'])
def find_lower(message):
    """Запуск скрипта по поиску отелей по низким ценам"""
    global data
    data['command'] = '/lower'
    bot.send_message(message.from_user.id, 'Давай начнем искать отели по низким ценам! \n Какой город выбираешь?')
    bot.register_next_step_handler(message, reg_town)


@bot.message_handler(commands=['higher'])
def find_higher(message):
    """Запуск скрипта по поиску отелей по высоким ценам"""
    global data
    data['command'] = '/higher'
    bot.send_message(message.from_user.id, 'Давай начнем искать отели по высоким ценам! \n Какой город выбираешь?')
    bot.register_next_step_handler(message, reg_town)


@bot.message_handler(commands=['price'])
def find_price(message):
    """Запуск скрипта по поиску отелей по определенным условиям ценам"""
    global data
    data['command'] = '/price'
    bot.send_message(message.from_user.id, 'Давай начнем искать отели по высоким ценам! \n Какой город выбираешь?')
    bot.register_next_step_handler(message, reg_town)


@bot.message_handler(commands=['history'])
def find_history(message):
    """Запуск скрипта по выдаче истории поиска"""
    global data
    data['command'] = '/history'
    with open('history.txt', 'r', encoding='utf-8') as file:
        reads = file.read()
        bot.send_message(message.from_user.id, 'Ваша история поиска: {}'.format(reads))


@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    """Ответ бота при любом сообщении клиента вне запущенных команд"""
    user = User(message)
    data.update({message.chat.id: user})

    bot.send_message(message.from_user.id, 'Попробуй /start')


def keyboard_create():
    """Создает клавиатуру для подтверждения введенных параметров"""
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    return keyboard


def keyboard_photos():
    """Создает клавиатуру для выбора необходимости фотографий"""
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='С фото', callback_data='С фото'))
    keyboard.add(types.InlineKeyboardButton(text='Без фото', callback_data='Без фото'))
    return keyboard


def reg_town(message):
    """ Проверка наличия города и выбор дальнейшего напрвления в зависимости от команды"""
    global data
    town = str(message.text)
    if town.isalpha():
        result = check_town(town)  # проверка наличия города
        if result:
            data['id_town'] = result[0]
            data['town'] = result[1]
            print(data['command'])
            if data['command'] != '/price':
                bot.send_message(message.from_user.id, 'Введи количество отелей')
                bot.register_next_step_handler(message, reg_hotels_num)
            else:  # для команды /price
                bot.send_message(message.from_user.id, 'Какой диапазон цен? Например: 700 2000')
                bot.register_next_step_handler(message, reg_price)
        else:
            bot.send_message(message.from_user.id, 'Такой город не найден!\nВведи название города')
            bot.register_next_step_handler(message, reg_town)
    else:
        bot.send_message(message.from_user.id, 'Название города должно состоять из букв')
        bot.register_next_step_handler(message, reg_town)


def reg_price(message):
    """ Проверка и назначение ценового диапазона для команды /price"""
    global data
    try:
        price = re.split(' ', message.text)
        if int(price[0]) and int(price[1]) and len(price) == 2:
            data['price'] = price
            bot.send_message(message.from_user.id, 'Как далеко от центра(км)? Например 5')
            bot.register_next_step_handler(message, reg_distance)
        else:
            raise ValueError
    except (ValueError, IndexError):
        bot.send_message(message.from_user.id, 'Попробуй ввести дипазон. Например: 700 2000')
        bot.register_next_step_handler(message, reg_price)


def reg_distance(message):
    """ Проверка и назначение удаленности от центра для команды /price"""
    global data
    try:
        data['distance'] = int(message.text)
        if data['distance'] in range(0, 25):
            bot.send_message(message.from_user.id, 'Введи количество отелей')
            bot.register_next_step_handler(message, reg_hotels_num)
        else:
            raise ValueError
    except (ValueError, IndexError):
        bot.send_message(message.from_user.id, 'Введи расстояние до 20 км')
        bot.register_next_step_handler(message, reg_distance)


def reg_hotels_num(message):
    """Проверка и назначение количества отелей для отображения"""
    global data
    try:
        data['hotels_num'] = int(message.text)
        if data['hotels_num'] not in range(1, 11):
            raise ValueError
        else:
            keyboard = keyboard_photos()
            bot.send_message(message.from_user.id, 'Нужны фотографии?', reply_markup=keyboard)
    except ValueError:
        bot.send_message(message.from_user.id, 'Выбери между 1  и  10 отелями')
        bot.register_next_step_handler(message, reg_hotels_num)


@bot.message_handler(func=lambda m: True)
def reg_num_photos(message):
    """Проверка и назначение количества фото для выдачи"""
    global data
    try:
        data['num_photos'] = int(message.text)
        if data['num_photos'] not in range(1, 7):
            raise ValueError
    except ValueError:
        bot.send_message(message.from_user.id, 'Не понял сколько! Отправлю тебе по 3 фото')
        data['num_photos'] = 3
    finally:
        keyboard = keyboard_create()
        if data['command'] != '/price':
            bot.send_message(message.from_user.id, 'Показать {} отелей в городе: {} с  {} фото'
                             .format(data['hotels_num'], data['town'], data['num_photos']),
                             reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id,
                             'Показать {} отелей в городе: {} \nс ценами от {} до {} \nв {} км от центра с {} фото'
                             .format(data['hotels_num'], data['town'], data['price'][0], data['price'][1],
                                     data['distance'], data['num_photos']), reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """Вывод кнопок на экран и запуск поиск с помощью Рапидапи"""
    global data
    if call.data == "yes":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Начинаю искать: )", reply_markup=None)

        print('Запуск поиска')
        all_data = search(data)
        if all_data == 'NO':  # В случае, если поиск не удался
            bot.send_message(call.message.chat.id,
                             'К сожалению ничего не нашлось!\nПопробуйте другие параметры'
                             '\n/lower - Отели по низким ценам '
                             '\n/higher - Отели по высоким ценам \n/price - Выбрать диапазон цен для отелей'
                             '\n/history - История запросов')

        else:  # В случае успешного поиска
            for num, value in all_data.items():
                bot.send_message(call.message.chat.id,
                                 '№{}. Отель: {} \n{} \nАдрес: {},\nОт центра: {},'
                                 '\nЦена за ночь: {}'.format(int(num) + 1, value['hname'], '⭐' * int(value['raiting']),
                                                             value['address'],
                                                             value['dist'], value['price']))
                if value.get('photos') is not None:
                    for ph in value['photos']:
                        bot.send_photo(call.message.chat.id, ph)
                elif value.get('photos') is None and data['num_photos'] != 0:
                    bot.send_message(call.message.chat.id, 'У Отеля {} нет фотографий'.format(value['hname']))

        data = {'town': '', 'price': [], 'command': '/lower', 'hotels_num': 0, 'distance': 20, 'id_town': '',
                'num_photos': 0}

    elif call.data == "no":  # В случае отказа пользователя от поиска
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
        'Попробуем еще раз!\n/lower - Отели по низким ценам'
        '\n/higher - Отели по высоким ценам\n/price - Выбрать диапазон цен для отелей \n/history - История запросов',
                              reply_markup=None)

    elif call.data == "Без фото":  # Кнопка обработки при отсутсвии необходимости загрузки фото
        keyboard = keyboard_create()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        text='Без фото', reply_markup=None)
        if data['command'] != '/price':
            bot.send_message(call.message.chat.id,
                             'Показать {} отелей в городе {}?'.format(data['hotels_num'], data['town']),
                             reply_markup=keyboard)
        else:
            bot.send_message(call.message.chat.id,
                             'Показать {} отелей в городе: {} \nс ценами от {} до {} \nв {} от центра'.format(
                                 data['hotels_num'], data['town'], data['price'][0], data['price'][1],
                                 data['distance']), reply_markup=keyboard)

    elif call.data == "С фото":  # Кнопка обработки при  необходимости загрузки фото
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
        'Сколько фотографий?', reply_markup=None)
        bot.register_next_step_handler(msg, reg_num_photos)


bot.polling(none_stop=True, interval=0)
