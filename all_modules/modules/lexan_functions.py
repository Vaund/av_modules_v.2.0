from utility import auto_, dict_search_user, bot, InlineKeyboardMarkup, \
    mass_search, InlineKeyboardButton, view_auto, unique_view,types


# lexan
def try_out(id_user, message_id):
    global buf_auto
    buf = []
    for k, v in auto_.items():
        flag = True
        for k1, v2 in dict_search_user[id_user]["dict"].items():
            if v2 == None:
                pass
            elif v2 in v[k1]:
                pass
            else:
                flag = False
        if flag:
            buf.append(v)
    if len(buf) <= 6:
        buf_auto = buf
        bot.delete_message(message_id=message_id, chat_id=id_user)
        view(buf)
        unique_views(id_user, buf)
        card(id_user, buf)
        return False
    else:
        return True


# lexan
def search(id_user, k_user, message_id=""):
    global buf_auto
    buf = []
    for k, v in auto_.items():
        flag = True
        for k1, v2 in dict_search_user[id_user]["dict"].items():
            if v2 == None:
                pass
            elif v2 in v[k1]:
                pass
            else:
                flag = False
        if flag:
            buf.append(v)
    if len(buf) <= 6:
        buf_auto = buf
        bot.delete_message(message_id=message_id, chat_id=id_user)
        view(buf)
        unique_views(id_user, buf)
        card(id_user, buf)
        return False
    else:
        keyb = InlineKeyboardMarkup()

        ind = mass_search.index(k_user)
        text = f"выберите {k_user}"
        buf_var = []
        for car in buf:
            buf_var.append(car[k_user])

        buf_var = sorted(list(set(buf_var)))
        for x in buf_var:
            keyb.add(InlineKeyboardButton(x, callback_data=f"cc{ind}@{buf_var.index(x)}"))

        dict_search_user[id_user]["m"] = buf_var
        if message_id == "":
            bot.send_message(id_user, text, reply_markup=keyb)
        if message_id != "":
            bot.edit_message_text(message_id=message_id, chat_id=id_user, text=text, reply_markup=keyb)


# lexan
def key_keyb(id_user, messsage_id=""):
    keyb = InlineKeyboardMarkup()
    for k1, v2 in dict_search_user[id_user]["dict"].items():
        if v2 == None:
            keyb.add(InlineKeyboardButton(k1, callback_data=f"kk{k1}"))
    if messsage_id != "":
        bot.edit_message_text(chat_id=id_user, message_id=messsage_id, text="Выберите следующий критерий",
                              reply_markup=keyb)
    else:
        bot.send_message(id_user, "Выберите критерий", reply_markup=keyb)


# lexa
def card(id_user, buf):
    for buffer in buf:
        keybb = InlineKeyboardMarkup()
        indx = buf.index(buffer)
        text = ''
        for a, b in buffer.items():
            if a != 'Массив картинок' and a != 'Описание' and a != 'Картинка' and a != 'Ссылки' and a != 'ID':
                text += f'{a}: {b}\n'
            if a == 'ID':
                id = b
            if a == 'Ссылки':
                text += f'<a href="{b}">🆔 {id} 🆔</a>\n'
            if a == 'Картинка':
                picture = b
        keybb.add(InlineKeyboardButton('Подробнее', callback_data=f'nn{str(indx)}'))
        bot.send_photo(id_user, picture, caption=text, reply_markup=keybb, parse_mode='HTML')


# lexan
def card_desc(id_user, num, msg_id):
    text = ''
    picture = []
    picture_list = []
    for a, b in buf_auto[num].items():
        if a != 'Массив картинок' and a != 'Картинка' and a != 'ID' and a != 'Ссылки':
            if a != 'Описание':
                text += f'{a}: {b}\n'
            else:
                text += f'\n{b}'
        if a == 'ID':
            id = b
        if a == 'Ссылки':
            text += f'\n<a href="{b}">🆔 {id} 🆔</a>'
        elif a == 'Массив картинок':
            for pp in b:
                pp = pp.replace(' ', '')
                picture_list.append(pp)
        else:
            pass
    for pict in picture_list:
        picture.append(types.InputMediaPhoto(f'{pict}', parse_mode='HTML',
                                             caption=text[0:1024] if picture_list[0] == pict else None))
    bot.delete_message(chat_id=id_user, message_id=msg_id)
    bot.send_media_group(id_user, picture)


# lexan
def view(buf):
    for i in buf:
        for a, b in i.items():
            if 'Ссылки' in a:
                id = b.split('/')[-1::]
                if id is not view_auto:
                    view_auto[id[0]] = {}
                    view_auto[id[0]]['Просмотров'] = 1
                    view_auto[id[0]]['Ссылка'] = b
                else:
                    view_auto[id[0]]['Просмотров'] += 1


# lexan
def unique_views(user_id, buf):
    for i in buf:
        for a, b in i.items():
            if 'Ссылки' in a:
                id = b.split('/')[-1::]
                if id[0] not in unique_view:
                    unique_view[id[0]] = {}
                    unique_view[id[0]]['Ссылка'] = b
                if user_id not in unique_view[id[0]]:
                    unique_view[id[0]][user_id] = {}
                    unique_view[id[0]][user_id] = 1
                else:
                    unique_view[id[0]][user_id] += 1
