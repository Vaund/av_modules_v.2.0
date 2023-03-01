import json
from utility import bot,dict_admins,inline_markup_n_admin,inline_markup_main,dict_data,dict_forward,InlineKeyboardMarkup, InlineKeyboardButton





# изменение админов
def keyb_change_ad():
    inline_markup_change_ad2 = InlineKeyboardMarkup()
    for k, v in dict_admins.items():
        inline_markup_change_ad2.add(InlineKeyboardButton((v['user_name']), callback_data=f'o1{k}'))
    return inline_markup_change_ad2

# удаление админов
def keyb_del_ad():
    inline_markup_del_ad2 = InlineKeyboardMarkup()
    for k, v in dict_admins.items():
        inline_markup_del_ad2.add(InlineKeyboardButton((v['user_name']), callback_data=f'n0{k}'))
    return inline_markup_del_ad2





# добваление администаторов
def new_admin(message):
    if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] is True:
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
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] is True:
            bot.send_message(message.chat.id, "Вы супер администратор", reply_markup=inline_markup_main)
    except:
        pass

    try:
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] is False:
            bot.send_message(message.chat.id, "Вы администратор")
    except:
        pass

    try:
        if message.chat.id not in dict_admins:
            bot.send_message(message.chat.id, "Вы не администратор")
    except:
        pass


# изменение имени админа
def new_name_ad(message):
    dict_admins[int(dict_data[message.chat.id])] = {'user_name': message.text, 'rights': dict_admins[int(dict_data[message.chat.id])]['rights']}
    bot.send_message(message.chat.id, "Администратор изменён")
    print(dict_admins)






