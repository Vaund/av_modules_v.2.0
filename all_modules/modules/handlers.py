import utility
from utility import search_dict, dict_search_user, bot, \
    view_auto, inline_markup, keybb, \
    dict_create_car, buf, inline_markup2 \
    , markup123, dict_change_car, my_car, \
    dict_data, mass_search, inline_markup3

from lexan_functions import key_keyb, search, try_out, card_desc
from lexan_functions import unique_view
from anna_functions import change_car, proverka_p, create_car


# Хендлер отлова /start
@bot.message_handler(commands=['start'])
def start(message=''):
    if message.text == '/start':
        bot.send_message(message.chat.id, "Добро пожаловать")
        dict_search_user[message.from_user.id] = {"dict": search_dict.copy(), "m": []}
        key_keyb(message.from_user.id)
        print(dict_search_user)


# lexan
@bot.message_handler(commands=['u_stats'])
def u_stats(message):
    if message.text == '/u_stats':
        for i in unique_view:
            flag = False
            text = f'Топ просмотров: '
            text_u = f'Уникальных просмотров: '
            count_view = len(unique_view[i]) - 1
            for a, b in unique_view[i].items():
                pass
                if a == 'Ссылка':
                    text_u += f'<a href="{b}">🆔 {i} 🆔</a>\n'
                    text += f'<a href="{b}">🆔 {i} 🆔</a>\n'
                if a != 'Ссылка' and b >= 3:
                    text += f'{a} : {b}\n'
                    flag = True
            if a != 'Ссылка':
                text_u += f'Просмотров: {count_view}\n'
                text += text_u

            if flag:
                bot.send_message(message.chat.id, text, parse_mode='HTML')
            else:
                bot.send_message(message.chat.id, text_u, parse_mode='HTML')


# lexan
@bot.message_handler(commands=['stats'])
def stats(message):
    if message.text == '/stats':
        text = ''
        for i in view_auto.keys():
            for a, b in view_auto[i].items():
                if a == 'Просмотров':
                    view_a = b
                    text_v = a
                if a == 'Ссылка':
                    text += f'<a href="{b}">🆔 {i} 🆔</a>, {text_v}: {view_a}\n'
        bot.send_message(message.chat.id, f'Статистика просмотров:\n{text}', parse_mode='HTML')


# anna
@bot.message_handler(commands=['check', 'yes', 'no', 'stop'])
def start(message):
    id = message.chat.id
    if message.text == '/check':
        if proverka_p(id) is True:
            bot.send_message(message.chat.id, "Админ меню", reply_markup=inline_markup)
        else:
            bot.send_message(message.chat.id, "Меню пользователя", reply_markup=keybb)
    if message.text == '/yes':
        dict_create_car[message.from_user.id] = buf.copy()
        create_car(message)
    if message.text == '/no' or message.text == "/stop":
        if proverka_p(id) is True:
            bot.send_message(message.chat.id, "Админ меню", reply_markup=inline_markup)
        else:
            bot.send_message(message.chat.id, "Меню пользователя", reply_markup=keybb)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, )
    id = call.message.chat.id
    flag = call.data[0:2]
    data = call.data[2:]
    print(call.data)
    # lexan
    if flag == "k1":
        search(call.from_user.id, message_id=call.message.message_id, k_user=data)

    if flag == 'c1':
        a, b = data.split("@")

        dict_search_user[call.from_user.id]["dict"][mass_search[int(a)]] = dict_search_user[call.from_user.id]["m"][
            int(b)]
        if try_out(call.from_user.id, call.message.message_id):
            key_keyb(call.from_user.id, messsage_id=call.message.message_id)
    if flag == 'n1':
        card_desc(call.from_user.id, num=int(data), msg_id=call.message.message_id)
    ###anna
    if flag == "em":
        print(data)
        bot.send_message(id, "Выберите автомобиль", reply_markup=inline_markup2)
    if flag == "ad":
        print(data)
        bot.send_message(id, "Хотите добавить новый автомобиль?", reply_markup=markup123)
    if flag == "mc":
        dict_change_car[id] = my_car[data]
        print(dict_change_car)
        bot.send_message(id, "Выберите что хотите изменить, для завершения и возврата в главное меню введите /stop",
                         reply_markup=inline_markup3)
    if flag == "22":
        dict_data[id] = data
        print(dict_data)
        msg = bot.send_message(id, "Введите  " + data)
        bot.register_next_step_handler(msg, change_car)
