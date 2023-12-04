from functions import *
from slovar import *
import datetime

admin_id = [1337136801, 1030020149, 6862396551]


def uf_start(message):
    """Начало общения с User"""
    try:
        chat_id = message.chat.id
        person_id = t_id_2_id[chat_id]
        person = creator_by_id(person_id)

        person_name = person.name

        msg = f'Привет, {person_name}!\nНажми «Меню» и посмотри команды.'

    except:
        user_name = message.from_user.first_name
        msg = f'Привет, {user_name}!\nНажми «Меню» и посмотри команды.'
        noname_id = message.from_user.id
        noname_lname = message.from_user.last_name
        noname_link = f'tg://user?id={noname_id}'
        info = (f'first_name: {user_name}\n'
                f'last_name: {noname_lname}\n'
                f'telegram id: {noname_id}\n'
                f'user link: {noname_link}')
        return [msg, info]
    return [msg]


def uf_who_is_on_duty(message):
    """Вывод пары дежурных"""

    duty_df = get_duty_DF()
    marker1 = True
    marker2 = True

    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%d.%m.%y")

    msg = f'Дежурные {formatted_date}\n'

    first = duty_df.loc[0, 'first']
    second = duty_df.loc[0, 'second']

    if (first == '[_]') or (first == 'Не назначено'):
        marker1 = False

    if (second == '[_]') or (second == 'Не назначено'):
        marker2 = False

    if marker1:
        msg += f'1) {first}\n'
    if marker2:
        msg += f'2) {second}\n'

    if not marker1 and not marker2:
        msg += f'Пока не назначены ¯\_(ツ)_/¯\n'

    msg += f'\n———ОКТУ Бот🤖———'
    return msg


def uf_my_info_acc(message):
    """Вывод информации обо мне"""

    chat_id = message.chat.id
    person_id = t_id_2_id[chat_id]
    person = creator_by_id(person_id)

    person_id = person.id
    person_t_id = person.t_id
    person_surname = person.surname
    person_name = person.name
    person_last_duty = person.last_duty
    person_count_duty = person.count_duty

    if person_last_duty == int('-1'):
        person_last_duty = f'Долг по дежурству'
    elif person_last_duty == 0:
        person_last_duty = f'Пока не дежурил(а)'
    else:
        date = datetime.datetime.fromtimestamp(person_last_duty)
        person_last_duty = date.strftime("%d.%m.%y")

    if int(person.t_id) in admin_id:
        is_admin = 'Да'
    else:
        is_admin = 'Нет'

    msg = (f'Твоя информация в БД 📙\n\n'
           f'◁По Боту 🤖▷\n'
           f'1) ID в БД: {person_id}\n'
           f'2) ID в телеге: {person_t_id}\n'
           f'3) Админ: {is_admin}\n\n'
           f'◁Личная Информация 🙂▷\n'
           f'1) Фамилия: {person_surname}\n'
           f'2) Имя: {person_name}\n\n'
           f'◁Дежурство 🧹▷\n'
           f'1) Последнее дежурство: {person_last_duty}\n'
           f'2) Количество дежурств: {person_count_duty}\n')

    return msg

def uf_my_info(message):

    try:
        msg = uf_my_info_acc(message)
    except:
        msg = f'Твоей информации нет в БД'

    return msg

def instruct(message):
    try:
        chat_id = message.chat.id
        person_id = t_id_2_id[chat_id]
        person = creator_by_id(person_id)

        person_name = person.name

    except:
        person_name = message.from_user.first_name


    msg = (f'Еще раз привет, {person_name}, это мини инструкция если я накосячил с описанием команд\n'
           f'1) • «/cmd1» - выведет тебе дежурных\n'
           f'2) • «/cmd2» - выведет тебе твою информацию по БД\n'
           f'3) • «/cmd3» - выведет тебе это сообщение\n\n')
    return msg
