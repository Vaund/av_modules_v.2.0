import utility
from utility import auto_, bot, dict_create_car, inline_markup \
    , dict_change_car, dict_data, inline_markup3, dict_admins, picture_mass,desc,message_id
import handlers
import json
# anna


copy_id = message_id.copy()

def proverka_p(idp):
    if idp in dict_admins:
        return dict_admins[idp]['rights']


def proverka_m(idm):
    if idm in auto_:
        return idm
# anna
def create_car(message):
    global message_id
    car_card = ''
    id_ = message.chat.id
    text = message.text
    flag = True
    if text != "Да" and text != "Нет" and text !='/yes':
        flag = False
    for k, v in dict_create_car[id_].items(): #перебирает словарь
        if v is not None:
            car_card += f'{k}: {str(v)}\n'
        if v is None and flag: #поиск элементов
            if message_id[0] != '' and message_id[1] != '':
                bot.edit_message_text(desc[k], id_, message_id[0])
                edit_card = bot.edit_message_caption(caption=car_card, chat_id=id_, message_id=message_id[1])
                if message:
                    bot.delete_message(id_, message.id)
                bot.register_next_step_handler(edit_card, create_car)
                break
            elif message_id[0] != '':
                    card = bot.edit_message_text(desc[k], id_, message_id[0])
                    if message.photo:
                        picture_card = bot.send_photo(id_, dict_create_car[id_]['Картинка'], car_card)
                        message_id.insert(1, picture_card.id)
                        if message:
                            bot.delete_message(id_, message.id)
                        bot.register_next_step_handler(picture_card, create_car)
                        break
                    if message:
                        bot.delete_message(id_, message.id)
                    bot.register_next_step_handler(card, create_car)
                    break
            else:
                card = bot.send_message(id_, desc[k])
                message_id.insert(0, card.id)
                bot.register_next_step_handler(card, create_car)
                if message:
                    bot.delete_message(id_, message.id)
                break

        elif v is None and not flag:
            if message.photo:
                try:
                    text = handlers.photo(message,'picture')
                except:
                    pass
            dict_create_car[id_][k] = text
            flag = True
        if dict_create_car[id_]['ID'] != None:
            username = message.from_user.username
            car_card += f'ID: {dict_create_car[id_]["ID"]}'
            if username == None:
                username = "Неизвестно"
            bot.send_photo("@testing_va",dict_create_car[id_]["Картинка"],f'{car_card}\nДобавил: @{username}')
            bot.edit_message_caption(caption=car_card, chat_id=id_, message_id=message_id[1])
            save_created_car(dict_create_car,id_)
            bot.send_message(id_,'Вы успешно добавиили машину')
            bot.send_message(message.chat.id, "Админ меню", reply_markup=inline_markup)
            picture_mass.clear()
            message_id = copy_id
            for i in dict_create_car[id_]["Массив картинок"]:
                bot.send_photo(id_,i)
    if text == "stop":
        for k, v in dict_create_car[id_].items():
            dict_create_car[id_][k] = None
        bot.send_message(message.chat.id, "Админ меню", reply_markup=inline_markup)

    print(dict_create_car[id_])

def save_created_car(dictionary,id):
    file_name = dictionary[id]['ID']
    with open(f"create_cars/{file_name}.json", 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)

    f = open(f"create_cars/{file_name}.json", 'r', encoding='utf-8')
    d = json.loads(f.read())
    f.close()



# anna
def change_car(message):
    id_ = message.from_user.id
    text = message.text
    if text != "stop" and text != "/start":
        for k, v in dict_change_car[id_].items():
            if k == dict_data[id_]:
                dict_change_car[id_][k] = text
        print(dict_change_car)
        bot.send_message(message.chat.id, "Выберите что ещё хотите изменить. Для завершения и возврата в главное меню введите stop", reply_markup=inline_markup3)
