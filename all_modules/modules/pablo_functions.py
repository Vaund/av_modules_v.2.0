import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from utility import bot, dict_admins, dict_forward
from utility import inline_markup_change_ad2, inline_markup_avto, inline_markup_n_admin, \
    inline_markup_main, inline_markup_change_ad, inline_markup_del_admin, inline_markup_change_admin


def keyb_change_ad():
    for k, v in dict_admins.items():
        inline_markup_change_ad2.add(InlineKeyboardButton(v['user_name'], callback_data=f'o1{v}'))


# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/start':
#         bot.send_message(message.chat.id, "Проверка на администратора...")
#         check_admin(message)
#         keyb_change_ad()
#
#     if message.text == '/newadmin':
#         if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
#             bot.send_message(message.chat.id, "Перешлите сообщение и укажите уровень прав нового администратора")
#         else:
#             bot.send_message(message.chat.id, "Отказано в доступе")
#     new_admin(message)
#
#     if message.text == '/stat':
#         if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
#             bot.send_message(message.chat.id, "Вот вся статистика")
#         else:
#             bot.send_message(message.chat.id, "Отказано в доступе")
#
#     if message.text == '/newcar':
#         if message.chat.id in dict_admins:
#             bot.send_message(message.chat.id, "Выберите действие с автомобилем", reply_markup=inline_markup_avto)
#         else:
#             bot.send_message(message.chat.id, "Отказано в доступе")
#
#     if message.text == '/help':
#         bot.send_message(message.chat.id, "Здесь должна быть помощь")


# добваление и изменение администаторов
def new_admin(message):
    if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
        try:
            forward_id = message.forward_from.id

            forward_username = message.forward_from.username

            dict_forward[message.chat.id] = forward_id, forward_username

            bot.send_message(message.chat.id, "Укажите уровень прав", reply_markup=inline_markup_n_admin)
        except:
            pass


# проверка на админа
def check_admin(message):
    try:
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
            bot.send_message(message.chat.id, "Вы супер администратор", reply_markup=inline_markup_main)
    except:
        pass

    try:
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == False:
            bot.send_message(message.chat.id, "Вы администратор")
    except:
        pass

    try:
        if message.chat.id not in dict_admins:
            bot.send_message(message.chat.id, "Вы не админостратор")
    except:
        pass


# удалание админов
def del_admin(message):
    forward_id = message.forward_from.id
    dict_admins.pop(forward_id)
    bot.send_message(message.chat.id, "Администратор удалён")
    print(dict_admins)

#
# @bot.callback_query_handler(func=lambda call: True)
# def query_handler(call):
#     bot.answer_callback_query(callback_query_id=call.id, )
#     id = call.message.chat.id
#     flag = call.data[0:2]
#     data = call.data[2:]
#
#     if flag == 'b0':
#         bot.send_message(id, "Вы действительно хотите изменить администратора?", reply_markup=inline_markup_change_ad)
#
#     if flag == 'o0':
#         bot.send_message(id, "Выберите администратора, которого хотите изменить", reply_markup=inline_markup_change_ad2)
#
#     if flag == 'o1':
#         # print(data)
#         for v in dict_admins.values():
#             bot.send_message(id, f"Имя пользователя: {v['user_name']} \nУровень прав: {v['rights']}",
#                              reply_markup=inline_markup_change_admin)
#
#     if flag == 't0':
#         bot.send_message(id, "Укажите новое имя")
#
#     if flag == 'y0':
#         bot.send_message(id, "Укажите права")
#
#     if flag == 'p0':
#         bot.send_message(id, "Отмена изменения")
#
#     if flag == 'c0':
#         # bot.send_message(id, call.message.id)
#         bot.send_message(id, "Вы действительно хотите удалить администратора?", reply_markup=inline_markup_del_admin)
#
#     if flag == 'j0':
#         del_a = bot.send_message(id, "Перешлите сообщение администратора, которого хотите удалить")
#         bot.register_next_step_handler(del_a, del_admin)
#
#     if flag == 'l0':
#         bot.send_message(id, "Отмена удаления")
#
#     if flag == 'f0':
#         for k, v in dict_forward.values():
#             pass
#         dict_admins[k] = {'user_name': v, 'rights': "False"}
#         bot.send_message(id, "Администратор добавлен")
#
#         print(dict_admins)
#         dict_forward.popitem()
#
#     if flag == 'g0':
#         for k, v in dict_forward.values():
#             pass
#         dict_admins[k] = {'user_name': v, 'rights': "True"}
#         bot.send_message(id, "Супер администратор добавлен")
#         print(dict_admins)
#         dict_forward.popitem()

#
# print("Ready")
# bot.infinity_polling()
