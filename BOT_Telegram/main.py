import telebot
from telebot import types
from rapid import search
import re


bot = telebot.TeleBot('1966024506:AAHwTlK-WOoE-YrNTwMJL-V-60thb0bzpX0')

town = ''
price = []
command = '/lower'
hotels_num = 0
distance = []


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     'ПРИВЕТ ! Я ПОМОГУ ТЕБЕ ВЫБРАТЬ ОТЕЛЬ!\n/lower - Отели по низким ценам '
                     '\n/higher - Отели по высоким ценам \n/price - Выбрать диапазон цен для отелей')


@bot.message_handler(commands=['lower'])
def find_lower(message):
    global command
    command = '/lower'
    bot.send_message(message.from_user.id, 'Давай начнем искать отели по низким ценам! \n Какой город выбираешь?')
    bot.register_next_step_handler(message, reg_town)


@bot.message_handler(commands=['higher'])
def find_higher(message):
    global command
    command = '/higher'
    bot.send_message(message.from_user.id, 'Давай начнем искать отели по высоким ценам! \n Какой город выбираешь?')
    bot.register_next_step_handler(message, reg_town)


@bot.message_handler(commands=['price'])
def find_price(message):
    global command
    command = '/price'
    bot.send_message(message.from_user.id, 'Давай начнем искать отели по высоким ценам! \n Какой город выбираешь?')
    bot.register_next_step_handler(message, reg_town)


def keyboard_create():
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    return keyboard


def reg_price(message):
    global price, town
    try:
        price = re.split('-',message.text)
        print (price)
        if int(price[0]) and int(price[1]) and len(price) == 2:
            bot.send_message(message.from_user.id, 'Как далеко от центра(км)? Например: 2-6')
            bot.register_next_step_handler(message, reg_distance)

        else:
            raise ValueError
    except (ValueError, IndexError):
        bot.send_message(message.from_user.id, 'Попробуй ввести дипазон. Например: 700-2000')
        bot.register_next_step_handler(message, reg_price)


def reg_distance(message):
    global price,town,command,distance
    try:
        distance = re.split(",|-|\n|:", message.text)
        print(distance)
        print(len(distance))
        if int(distance[0]) in range(0,25) and int(distance[1]) in range(0,25) and len(distance) == 2:
            keyboard = keyboard_create()
            bot.send_message(message.from_user.id, 'Показать {} отелей в городе: {} \nс ценами от {} до {} \nв {} от центра?'.format(hotels_num, town,price[0],price[1],distance[0]),
                             reply_markup=keyboard)

        else:
            raise ValueError
    except (ValueError, IndexError):
        bot.send_message(message.from_user.id, 'Попробуй ввести дипазон. Например: 1 - 5')
        bot.register_next_step_handler(message, reg_distance)


def reg_town(message):
    global town, command
    z = str(message.text)
    if z.isalpha():
        town = z
        bot.send_message(message.from_user.id, 'Введи количество отелей')
        bot.register_next_step_handler(message, reg_hotels_num)
    else:
        bot.send_message(message.from_user.id, 'Попробуй ввести буквы')
        bot.register_next_step_handler(message, reg_town)



@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Попробуй /start')


def reg_hotels_num(message):
    global  town,hotels_num, command
    try:
        hotels_num = int(message.text)
        if  hotels_num not in range(1,11):
            raise ValueError
        if command == '/price':
            bot.send_message(message.from_user.id, 'Какой диапазон цен? Например: 700-2000')
            bot.register_next_step_handler(message, reg_price)
        else:
            print(hotels_num)
            keyboard = keyboard_create()
            bot.send_message(message.from_user.id, 'Показать {} отелей в городе: {}?'.format(hotels_num, town), reply_markup=keyboard)
    except ValueError:
        bot.send_message(message.from_user.id, 'Введите число от 1 до 10')
        bot.register_next_step_handler(message, reg_hotels_num)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global town, hotels_num,command,price,distance
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Начинаю искать: )')
        print(town)
        print(type(town))
        print('количество отелей:', str(hotels_num))
        res = search(town,hotels_num,command,price, distance)
        town = ''
        price = []
        command = '/lower'
        hotels_num = 0
        distance = []
        if res  == 'NO':
            bot.send_message(call.message.chat.id,
                             'К соЖалению ничего не нашлось!\nПопробуйте другие праметры\n/lower - Отели по низким ценам '
                             '\n/higher - Отели по высоким ценам \n/price - Выбрать диапазон цен для отелей')
        else:
            for i, k in res.items():
                bot.send_message(call.message.chat.id,
                                 'Отель: {} \n{} \nАдрес: {},\nОт центра: {},'
                    '\nЦена за ночь: {}'.format(k['hname'],'⭐'*int(k['raiting']),k['address'],k['dist'],k['price']))

    elif call.data == "no":
        bot.send_message(call.message.chat.id,
                         'Попробуем еще раз!\n/lower - Отели по низким ценам'
                         '\n/higher - Отели по высоким ценам\n/price - Выбрать диапазон цен для отелей')



bot.polling(none_stop=True, interval=0)
