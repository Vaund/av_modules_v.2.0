from utility import auto_, bot, dict_create_car, inline_markup \
    , dict_change_car, dict_data, inline_markup3, dict_admins


# anna
def proverka_p(idp):
    if idp in dict_admins:
        return dict_admins[idp]['rights']


def proverka_m(idm):
    if idm in auto_:
        return idm


# anna
def create_car(message):
    id_ = message.from_user.id
    text = message.text
    print(message)
    flag = True
    if text != "да" and text != "нет":
        flag = False
    for k, v in dict_create_car[id_].items():  # перебирает словарь
        if v is None and flag:  # поиск элементов
            if k == 'Картинка':
                m = bot.send_message(id_, f"Отправьте картинку")
                bot.register_next_step_handler(m, create_car)
                break
            if k == 'Массив картинок':
                m = bot.send_message(id_, f"Отправьте несколько картинок")
                bot.register_next_step_handler(m, create_car)
                break
            if k != 'Картинка' and k != 'Массив картинок':
                m = bot.send_message(id_, f"Введите {k}")
                bot.register_next_step_handler(m, create_car)
                break
        elif v is None and not flag:
            if k == 'Картинка':
                try:
                    text = message.photo[-1].file_id
                except:
                    print('Отправлена не картинка')
            if k == 'Массив картинок':
                mass_picture = []
                for i in range(0, 10):
                    try:
                        mass_picture.append(message.media_group_id)
                        print(mass_picture)
                    except:
                        print('pppp')
                for a in mass_picture:
                    bot.send_media_group(id_, a)
            dict_create_car[id_][k] = text

            flag = True
    if text == "stop":
        for k, v in dict_create_car[id_].items():
            dict_create_car[id_][k] = None
        bot.send_message(message.chat.id, "Админ меню", reply_markup=inline_markup)

    print(dict_create_car[id_])


# anna
def change_car(message):
    id_ = message.from_user.id
    text = message.text
    if text != "stop" and text != "/start":
        for k, v in dict_change_car[id_].items():
            if k == dict_data[id_]:
                dict_change_car[id_][k] = text
        print(dict_change_car)
        bot.send_message(message.chat.id,
                         "Выберите что ещё хотите изменить. Для завершения и возврата в главное меню введите stop",
                         reply_markup=inline_markup3)
