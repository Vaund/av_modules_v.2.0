import json
from utility import search_dict, dict_search_user, bot, \
    view_auto, inline_markup, keybb, \
    dict_create_car, buf, inline_markup2 \
    , markup123, dict_change_car, my_car, \
    dict_data, mass_search, inline_markup3,dict_admins,inline_markup_avto,inline_markup_change_ad\
    ,inline_markup_change_admin, \
    inline_markup_del_admin,dict_forward,inline_markup_rights_admin,inline_markup_delete_admin,dict_del,picture_mass

import anna_functions
from anna_functions import change_car, proverka_p,create_car
from pablo_functions import check_admin,keyb_change_ad,new_admin,new_name_ad,keyb_del_ad
from lexan_functions import key_keyb, search, try_out, card_desc
from lexan_functions import unique_view

@bot.message_handler(commands=['admin_start','new_admin','stat','new_car','help',''])
def admin_start(message):
    if message.text == '/admin_start':
        bot.send_message(message.chat.id, "Проверка на администратора...")
        check_admin(message)

    if message.text == '/help':
        bot.send_message(message.chat.id, "Здесь должна быть помощь")


# Хендлер отлова /start
@bot.message_handler(commands=['start'])
def start(message=''):
    if message.text == '/start':
        bot.send_message(message.chat.id, "Добро пожаловать")
        dict_search_user[message.from_user.id] = {"dict": search_dict.copy(), "m": []}
        key_keyb(message.from_user.id)
        print(dict_search_user)

#anna
@bot.message_handler(content_types=['photo'])
def photo(message,flag=''):
    if flag == 'picture':
        picture_mass.append(message.photo[-1].file_id)
        return message.photo[-1].file_id
    for i in range(0,3):
        try:
            picture = message.photo[-1].file_id
            picture_mass.append(picture)
        except:
            print('ppp')
    try:
        picture = list(set(picture_mass))
        dict_create_car[message.from_user.id]['Массив картинок'] = picture
        print(dict_create_car)
    except:
        print('user id не привязан к словарю')
@bot.message_handler(commands=['u_stats'])
def u_stats(message):
    if message.text == '/u_stats' and message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
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
    else:
        bot.send_message(message.chat.id,'Пшол вон')
# lexan
@bot.message_handler(commands=['stats','u_stats'])
def stats(message):
    if message.text == '/stats' and message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
        text = ''
        for i in view_auto.keys():
            for a, b in view_auto[i].items():
                if a == 'Просмотров':
                    view_a = b
                    text_v = a
                if a == 'Ссылка':
                    text += f'<a href="{b}">🆔 {i} 🆔</a>, {text_v}: {view_a}\n'
        bot.send_message(message.chat.id, f'Статистика просмотров:\n{text}', parse_mode='HTML')
    else:
        bot.send_message(message.chat.id,'Пшол вон')



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
    if flag == "kk":
        search(call.from_user.id, message_id=call.message.message_id, k_user=data)

    if flag == 'cc':
        a, b = data.split("@")

        dict_search_user[call.from_user.id]["dict"][mass_search[int(a)]] = dict_search_user[call.from_user.id]["m"][
            int(b)]
        if try_out(call.from_user.id, call.message.message_id):
            key_keyb(call.from_user.id, messsage_id=call.message.message_id)
    if flag == 'nn':
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
    #pablo
    if flag == 'c1':
        for k, v in dict_admins.items():
            bot.send_message(id, f"Имя пользователя: {v['user_name']} \nУровень прав: {v['rights']}")
        bot.edit_message_text("Вот все администраторы", chat_id=id, message_id=call.message.message_id)

    if flag == 'b0':
        bot.edit_message_text("Вы действительно хотите изменить администратора?", chat_id=id,
                              message_id=call.message.message_id, reply_markup=inline_markup_change_ad)


    if flag == 'o0':
        bot.edit_message_text("Выберите администратора, которого хотите изменить", chat_id=id,
                              message_id=call.message.message_id, reply_markup=keyb_change_ad())




    if flag == 'o1':
        dict_data[id] = data
        print("dict_data", dict_data)
        bot.edit_message_text(f"Имя пользователя: {dict_admins[int(data)]['user_name']} \nУровень прав: "
                             f"{dict_admins[int(data)]['rights']}", chat_id=id,
                              message_id=call.message.message_id, reply_markup=inline_markup_change_admin)




    if flag == 't0':
        new_name = bot.edit_message_text("Укажите новое имя", chat_id=id, message_id=call.message.message_id)
        bot.register_next_step_handler(new_name, new_name_ad)
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)


    if flag == 'y0':
        bot.edit_message_text("Укажите права", chat_id=id, message_id=call.message.message_id,
                              reply_markup=inline_markup_rights_admin)

        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)

    if flag == 't1':
        dict_admins[int(dict_data[id])] = {'user_name': dict_admins[int(dict_data[id])]['user_name'], 'rights': False}
        bot.edit_message_text("Администратор добавлен", chat_id=id, message_id=call.message.message_id)
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)


    if flag == 'y1':
        dict_admins[int(dict_data[id])] = {'user_name': dict_admins[int(dict_data[id])]['user_name'], 'rights': True}
        bot.edit_message_text("Супер администратор добавлен", chat_id=id, message_id=call.message.message_id)
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)


    if flag == 'p0':
        bot.send_message(id, "Отмена изменения")


    if flag == 'c0':
        # bot.send_message(id, call.message.id)
        bot.edit_message_text("Вы действительно хотите удалить администратора?", chat_id=id,
                              message_id=call.message.message_id, reply_markup=inline_markup_del_admin)


    if flag == 'j0':
        bot.edit_message_text("Выберите администратора, которого хотите удалить", chat_id=id,
                              message_id=call.message.message_id, reply_markup=keyb_del_ad())


    if flag == 'n0':
        dict_del[id] = data
        print(dict_del)
        bot.edit_message_text(f"Имя пользователя: {dict_admins[int(data)]['user_name']} \nУровень прав: "
                              f"{dict_admins[int(data)]['rights']}", chat_id=id,
                              message_id=call.message.message_id, reply_markup=inline_markup_delete_admin)


    if flag == 'n1':
        dict_admins.pop(int(dict_del[id]))
        bot.edit_message_text("Администратор удалён", chat_id=id, message_id=call.message.message_id)
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)


    if flag == 'l0':
        bot.send_message(id, "Отмена удаления")


    if flag == 'f0':
        for k, v in dict_forward.values():
            pass
        dict_admins[k] = {'user_name': v, 'rights': False}
        bot.send_message(id, "Администратор добавлен")
        # print(dict_admins[forward_id])
        # print(forward_id)
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)
        dict_forward.popitem()
        # print(dict_forward)

    if flag == 'g0':
        for k, v in dict_forward.values():
            pass
        dict_admins[k] = {'user_name': v, 'rights': True}
        bot.send_message(id, "Супер администратор добавлен")
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)
        dict_forward.popitem()
