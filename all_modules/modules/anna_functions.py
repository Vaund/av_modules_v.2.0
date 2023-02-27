from utility import auto_, bot, dict_create_car, inline_markup \
    , dict_change_car, dict_data, inline_markup3, dict_admins, picture_mass
import handlers
import json

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
    flag = True
    if text != "Да" and text != "Нет" and text !='/yes':
        flag = False
    for k, v in dict_create_car[id_].items(): #перебирает словарь
        if v is None and flag: #поиск элементов
            if k == 'Картинка':
                pass
            m = bot.send_message(id_, f"Введите {k}")
            bot.register_next_step_handler(m, create_car)
            break
        elif v is None and not flag:
            if k == 'Картинка':
                try:
                    text = handlers.photo(message,'picture')
                except:
                    pass
            dict_create_car[id_][k] = text
            flag = True
        if dict_create_car[id_]['ID'] != None:
            save_created_car(dict_create_car,id_)
            bot.send_message(id_,'Вы успешно добавиили машину')
            picture_mass.clear()
            bot.send_message(message.chat.id, "Админ меню", reply_markup=inline_markup)

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
