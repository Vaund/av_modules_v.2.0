import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import gspread

import dotenv
import os

dotenv.load_dotenv(".env")
bot = telebot.TeleBot(os.environ["TOKEN"])
gc = gspread.service_account(os.environ["json_creds"])
sht2 = gc.open_by_url(os.environ["google_sheet"])
# bot = telebot.TeleBot('5852383239:AAGrmzgosJc2uAupjgWdvh2_1nWxc28-rII')
# gc = gspread.service_account(filename="calm-vine-332204-924334d7332a.json")
# sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1qhAMkYQ11Q7dr_ImtpjnqtSwFDsOy1Deu1mE58nTEys/edit#gid=0')
list_of_lists = sht2.worksheet("av_by").get_all_values()


mass_search = ['Марка', 'Год выпуска', 'Объем двигателя', 'Тип двигателя', 'Тип авто', 'Геолокация продавца']
search_dict = {'Марка': None, 'Год выпуска': None, 'Объем двигателя': None, 'Тип двигателя': None, 'Тип авто': None,
               'Геолокация продавца': None}

key_mass = ['Марка', 'Модель', 'Картинка', 'Год выпуска', 'Обьем двигателя', 'Тип двигателя', 'Пробег', 'Тип авто',
            'Цена', 'Геолокация продавца', 'Инф о двигателе VIN', 'Массив картинок', 'Описание ', 'ID']
my_car = {"103365747": {'Марка': 'Nissan', 'Модель': 'Primera',
                        'Картинка': 'https://avcdn.av.by/advertmedium/0001/6570/5004.jpg', 'Год выпуска': '1991г.',
                        'Обьем двигателя': ' 2.0л', 'Тип двигателя': ' дизель', 'Пробег': ' 331\u2009000км',
                        'Тип авто': 'седан, передний привод, другой', 'Цена': '3300р.',
                        'Геолокация продавца': 'Смолевичи, Минская обл.', 'Инф о двигателе VIN': 'VIN',
                        'Массив картинок': ['https://avcdn.av.by/advertmedium/0001/6570/5004.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5019.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5029.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5014.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5034.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5009.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5024.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5039.jpg'],
                        'Описание ': 'Все недостатки указаны на фотоЗа время моего владения было сделано:Замена антифризаШлифовка головы Замена маслосьёмных колпачков(машина не дымит)Заменён к-т приводного ремняЗамена ремня грм ( замена на 322000)Замена штатных динамиков на более по подвеске ничего не гремит и не стучит Заменен аккумулятор (есть гарантия)Корректор фар и регулировка зеркал рабочее Все остальные вопросы по телефону Торг у капота Тех.осмотр до сентября 2023'},
          "103365748": {'Марка': 'Тойота', 'Модель': 'Primera',
                        'Картинка': 'https://avcdn.av.by/advertmedium/0001/6570/5004.jpg', 'Год выпуска': '1990г.',
                        'Обьем двигателя': ' 2.9л', 'Тип двигателя': ' дизель', 'Пробег': ' 331\u2009000км',
                        'Тип авто': 'седан, передний привод, другой', 'Цена': '3900р.',
                        'Геолокация продавца': 'Смолевичи, Минская обл.', 'Инф о двигателе VIN': 'VIN',
                        'Массив картинок': ['https://avcdn.av.by/advertmedium/0001/6570/5004.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5019.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5029.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5014.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5034.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5009.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5024.jpg',
                                            ' https://avcdn.av.by/advertmedium/0001/6570/5039.jpg'],
                        'Описание ': 'Все недостатки указаны на фотоЗа время моего владения было сделано:Замена антифризаШлифовка головы Замена маслосьёмных колпачков(машина не дымит)Заменён к-т приводного ремняЗамена ремня грм ( замена на 322000)Замена штатных динамиков на более по подвеске ничего не гремит и не стучит Заменен аккумулятор (есть гарантия)Корректор фар и регулировка зеркал рабочее Все остальные вопросы по телефону Торг у капота Тех.осмотр до сентября 2023'}}

dict_search_user = {}
buf_auto = []

view_auto = {}
unique_view = {}
dict_data = {}

auto_ = {}
dict_admins = {}
dict_admins[760148226] = {'user_name': 'UITAAP', 'rights': True}
dict_admins[665909535] = {'user_name': 'lexan4ik', 'rights': True}
dict_admins[657287224] = {"user_name": "Lesha", "rights": True}

buf = dict.fromkeys(key_mass)

dict_create_car = {}

dict_change_car = {}

for el in list_of_lists[1:]:
    auto_[el[13]] = {}
    for i in range(0, 15):

        if list_of_lists[0][i] == 'Массив картинок':
            auto_[el[13]][list_of_lists[0][i]] = el[i].split(',')
        else:

            auto_[el[13]][list_of_lists[0][i]] = el[i]
    if el[8] and el[6]:
        for n in range(2, len(el)):
            price = el[8]
            decode_price = price.encode("ascii", "ignore")
            decode_price = decode_price.decode()
            auto_[el[13]]['Цена'] = decode_price.replace('.', '')

            mileage = el[6]
            decode_mileage = mileage.encode("ascii", "ignore")
            decode_mileage = decode_mileage.decode()
            auto_[el[13]]['Пробег'] = decode_mileage.replace('.', '')




keybb = InlineKeyboardMarkup()
keybb.add(InlineKeyboardButton('Изменить информацию об автомобиле', callback_data='em'))


inline_markup = InlineKeyboardMarkup()
inline_markup.add(InlineKeyboardButton('Изменить информацию об автомобиле', callback_data='em'))
inline_markup.add(InlineKeyboardButton("Добавить новый автомобиль", callback_data="ad"))


markup123 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("/yes")
button2 = types.KeyboardButton("/no")
markup123.add(button1,button2)



inline_markup2 = InlineKeyboardMarkup()
for x in my_car:
    inline_markup2.add(InlineKeyboardButton(x, callback_data="mc" + x))


key_mass.remove("ID")
inline_markup3 = InlineKeyboardMarkup()
for x in key_mass:
    inline_markup3.add(InlineKeyboardButton(x, callback_data="22" + x))