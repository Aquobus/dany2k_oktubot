from functions import *
from slovar import *
import datetime

admin_id = [1337136801, 1030020149, 6862396551]


def start(message):
    if message.from_user.id in admin_id:
        chat_id = message.chat.id
        person_id = t_id_2_id[chat_id]
        person = creator_by_id(person_id)

        person_name = person.name

        msg = f'Привет, {person_name}!\nКоманды в «Меню»'
        return msg
    else:
        return 'Ты не являешься администратором ಠ_ಠ'


def create_day(message, array):
    """Создание пары дежурных"""

    if message in admin_id:
        duty = take_duty_persons(array)
        if len(duty) == 2:
            array = []
            current_date = datetime.date.today()
            formatted_date = current_date.strftime("%d.%m.%y")

            string = f'Сегодня {formatted_date} дежурят: {duty[0]} и {duty[1]}'
            output = [string, [duty[0], duty[1]]]
            if f'Сегодня' in duty:
                output = duty
            if 'Увы' in duty:
                output = duty
            return output
        else:
            array = []
            current_date = datetime.date.today()
            formatted_date = current_date.strftime("%d.%m.%y")

            string = f'Сегодня {formatted_date} дежурит: {duty[0]}'
            output = [string, [duty[0]]]
            if f'Сегодня' in duty:
                output = duty
            if 'Увы' in duty:
                output = duty
            return output

    else:
        return 'Ты не являешься администратором ಠ_ಠ'


def duty_false(message):
    """Запись недеружившей пары"""

    if message.chat.id in admin_id:

        couple_df = get_duty_DF()
        fst = couple_df.loc[0, 'first']
        snd = couple_df.loc[0, 'second']
        duty_couple = [fst, snd]

        success_marker1 = False
        success_marker2 = False

        surname1 = ''
        surname2 = ''
        msg = ''

        try:
            surname1 = duty_couple[0]
            unsucces(surname1)
        except:
            msg += 'Фамилия первого ученика некорректна!\n'
            success_marker1 = True

        try:
            surname2 = duty_couple[1]
            unsucces(surname2)
        except:
            msg += 'Фамилия второго ученика некорректна!\n'
            success_marker2 = True

        if success_marker1:
            msg += 'Не удалось сохранить первого ученика\n'
        else:
            msg += f'{surname1} теперь в списочке!\n'
            couple_df.loc[0, 'first'] = '[_]'

        if success_marker2:
            msg += 'Не удалось сохранить второго ученика\n'
        else:
            msg += f'{surname2} теперь в списочке!\n'
            couple_df.loc[0, 'second'] = '[_]'

        return msg

    else:
        return 'Ты не являешься администратором ಠ_ಠ'


def duty_true(message):
    """Запись дежурившей пары"""

    if message.chat.id in admin_id:
        couple_df = get_duty_DF()
        fst = couple_df.loc[0, 'first']
        snd = couple_df.loc[0, 'second']
        duty_couple = [fst, snd]

        success_marker1 = False
        success_marker2 = False

        surname1 = ''
        surname2 = ''
        msg = ''

        try:
            surname1 = duty_couple[0]
            success(surname1)
        except:
            msg += 'Фамилия первого ученика некорректна!\n'
            success_marker1 = True

        try:
            surname2 = duty_couple[1]
            success(surname2)
        except:
            msg += 'Фамилия второго ученика некорректна!\n'
            success_marker2 = True

        if success_marker1:
            msg += 'Не удалось сохранить первого ученика\n'
        else:
            msg += f'{surname1} теперь в списочке!\n'
            couple_df.loc[0, 'first'] = '[_]'

        if success_marker2:
            msg += 'Не удалось сохранить второго ученика\n'
        else:
            msg += f'{surname2} теперь в списочке!\n'
            couple_df.loc[0, 'second'] = '[_]'

        return msg

    else:
        return 'Ты не являешься администратором ಠ_ಠ'


def duty_skip(message):
    """Пропуск дежурных если Данитук накосячил"""

    if message.chat.id in admin_id:
        df = get_duty_DF()
        df.loc[0, 'first'] = '[_]'
        df.loc[0, 'second'] = '[_]'
        df.to_excel('duty_list.xlsx', index=False)
        return 'Ученики убраны из бд'
    else:
        return 'Ты не являешься администратором ಠ_ಠ'


def who_is_on_duty(message):
    """Вывод пары дежурных"""

    if message.chat.id in admin_id:
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
    else:
        return 'Ты не являешься администратором ಠ_ಠ'


def instruct(message):
    if message.chat.id in admin_id:
        msg = (
            f'В общем этот Бот как произведение искусства должен работать аккуратно, поэтому не спамь командами пожалуйста\n'
            f'Чтобы создать дежурных нужно:\n'
            f'• Выбрать команду «/cmd1»\n'
            f'• Выбрать всех кто есть по порядку, просто смотри на фамилию в кнопке и проверяй есть ли он или нет\n'
            f'• Когда нашел отмечай и так пока не проверишь всех\n'
            f'• Когда всех отметил нажимай "Завершить" и сообщай группе дежурных\n'
            f'• Если человек или группа отказываются дежурить то выбирай команду «/cmd2»\n'
            f'• Начинай операцию заново (непродумано но ничего)\n'
            f'• Если все ок, то позже проверь чтобы они отдежурили и когда все ок то выбирай команду «/cmd3»\n'
            f'• Если ошибся человеком и он попал в дежурство то выбери команду «/cmd4»')
        return msg
    else:
        return 'Ты не являешься администратором ಠ_ಠ'
