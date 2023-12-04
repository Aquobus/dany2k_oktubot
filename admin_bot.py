import telebot
import time
import datetime
from telebot import types
import bot_functions as BF

ADMIN_TOKEN = '6050674470:AAF3jnJHpvPOOBBvAw9uRMrH7qLnVx7ehYI'
array = []
admin_id = [1337136801, 1030020149, 6862396551]
bot = telebot.TeleBot(ADMIN_TOKEN)

def time_refract(start_time, end_time):
    """Функция перерабатывает время в удобное у восприятию"""

    if end_time < start_time:
        return f'Конечное время мешьше чем начальное!'

    else:
        time = end_time-start_time

        days = int(round(time//86400, 0))

        time %= 86400

        hours = int(round(time//3600, 0))

        time %= 3600

        minutes = int(round(time//60, 0))

        time %= 60

        seconds = int(round(time, 0))

        msg = (f'Бот проработал🕔:\n'
               f'Дней:     {days}\n'
               f'Часов:   {hours}\n'
               f'Минут:  {minutes}\n'
               f'Секунд: {seconds}')

        return msg

@bot.message_handler(commands=['start'])
def start(message):
    msg = BF.start(message)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['cmd1', 'create'])
def cmd1(message):
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%d.%m.%y")

    keyboard = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text='Баюнц', callback_data='0')
    button2 = types.InlineKeyboardButton(text='Бурлака', callback_data='1')
    button3 = types.InlineKeyboardButton(text='Вердян', callback_data='2')
    button4 = types.InlineKeyboardButton(text='Виноградов', callback_data='3')
    button5 = types.InlineKeyboardButton(text='Волкова', callback_data='4')
    button6 = types.InlineKeyboardButton(text='Володин', callback_data='5')
    button7 = types.InlineKeyboardButton(text='Гостюхин', callback_data='6')
    button8 = types.InlineKeyboardButton(text='Гузиев', callback_data='7')
    button9 = types.InlineKeyboardButton(text='Жильцов', callback_data='8')
    button10 = types.InlineKeyboardButton(text='Игнатьев', callback_data='9')
    button11 = types.InlineKeyboardButton(text='Исаев', callback_data='10')
    button12 = types.InlineKeyboardButton(text='Колмаков', callback_data='11')
    button13 = types.InlineKeyboardButton(text='Костырин', callback_data='12')
    button14 = types.InlineKeyboardButton(text='Лапшин', callback_data='13')
    button15 = types.InlineKeyboardButton(text='Лопатюк', callback_data='14')
    button16 = types.InlineKeyboardButton(text='Любин', callback_data='15')
    button17 = types.InlineKeyboardButton(text='Маилян', callback_data='16')
    button18 = types.InlineKeyboardButton(text='Машрабов', callback_data='17')
    button19 = types.InlineKeyboardButton(text='Ротарь', callback_data='18')
    button20 = types.InlineKeyboardButton(text='Тарасов', callback_data='19')
    button21 = types.InlineKeyboardButton(text='Толмачёв', callback_data='20')
    button22 = types.InlineKeyboardButton(text='Трифонов', callback_data='21')
    button23 = types.InlineKeyboardButton(text='Чулиев', callback_data='22')

    blank_button = types.InlineKeyboardButton(text='◁▷',callback_data='blink')

    finish_button = types.InlineKeyboardButton(text='Завершить', callback_data='finish')

    keyboard.add(button1,
                 button2,
                 button3,
                 button4,
                 button5,
                 button6,
                 button7,
                 button8,
                 button9,
                 button10,
                 button11,
                 button12,
                 button13,
                 button14,
                 button15,
                 button16,
                 button17,
                 button18,
                 button19,
                 button20,
                 button21,
                 button22,
                 button23, row_width=2)
    keyboard.add(blank_button, row_width=1)

    keyboard.add(finish_button, row_width=1)

    bot.send_message(message.chat.id, f'{formatted_date}\nВыбери фамилии присутствующих:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    button_value = call.data

    if button_value != 'finish' and button_value == 'blink':
        if button_value == 'blink':
            pass
        else:
            if int(button_value) not in array:
                array.append(int(button_value))

    else:
        msg = BF.create_day(call.message.chat.id, array)
        bot.send_message(call.message.chat.id, msg)
        array.clear()


@bot.message_handler(commands=['cmd2', 'bad'])
def cmd2(message):
    msg = BF.duty_false(message)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['cmd3', 'good'])
def cmd3(message):
    msg = BF.duty_true(message)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['cmd4', 'skip'])
def cmd4(message):
    msg = BF.duty_skip(message)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['cmd5', 'check'])
def msg5(message):
    msg = BF.who_is_on_duty(message)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['cmd6', 'info'])
def cmd6(message):
    msg = BF.instruct(message)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['cmd7', 'call'])
def cmd7(message):
    chat_id = message.chat.id
    if chat_id in admin_id:
        bot.send_message(chat_id, 'Кому написать сообщение?', reply_markup=create_keyboard())
    else:
        bot.send_message(chat_id, f'Ты не являешься администратором ಠ_ಠ')

def create_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Данику')
    button2 = types.KeyboardButton(text='Асану')
    button3 = types.KeyboardButton(text='Насте')
    button4 = types.KeyboardButton(text='Всем')
    markup.add(button1, button2, button3, button4)
    return markup
def get_user_id(username):
    if username == 'Данику':
        return '1337136801'
    elif username == 'Асану':
        return '1030020149'
    elif username == 'Насте':
        return '6862396551'

@bot.message_handler(func=lambda mesage: mesage.text in ['Данику', 'Асану', 'Насте', 'Всем'])
def handle_selection(message):
    chat_id = message.chat.id
    if chat_id in admin_id:
        if message.text == 'Всем':
            send_to_all_except_sender(chat_id)
        else:
            add = '(Личное)'
            send_message(chat_id, get_user_id(message.text), add, is_all=True)
    else:
        bot.send_message(chat_id, f'Ты не можешь писать администраторам ಠ‿ಠ')

def send_to_all_except_sender(sender_chat_id):
    users = ['1337136801', '1030020149', '6862396551']
    add = '(Рассылка)'
    is_all = True
    for user_id in users:
        if str(sender_chat_id) != user_id:
            send_message(sender_chat_id, user_id, add, is_all)
            is_all = False


def send_message(sender_chat_id, receiver_chat_id, add, is_all):
    if is_all:
        bot.send_message(sender_chat_id, 'Напиши сообщение для отправки', reply_markup=types.ReplyKeyboardRemove())
    else:
        pass

    bot.register_next_step_handler_by_chat_id(sender_chat_id,
                                              lambda message: send_text_message(message, receiver_chat_id, sender_chat_id, add))


def send_text_message(message, receiver_chat_id, sender_chat_id, add):
    sender = f'{sender_chat_id}'
    if int(sender_chat_id) == 1337136801:
        sender = 'Даника'
    elif int(sender_chat_id) == 1030020149:
        sender = 'Асана'
    elif int(sender_chat_id) == 6862396551:
        sender = 'Насти'
    text = f'Сообщение от {sender}, {add}:\n\n'
    text += f'— {message.text}'
    try:
        for_people = ''
        if int(receiver_chat_id) == 1337136801:
            for_people = ' Данику'
        elif int(receiver_chat_id) == 1030020149:
            for_people = ' Асану'
        elif int(receiver_chat_id) == 6862396551:
            for_people = ' Насте'
        bot.send_message(receiver_chat_id, f'{text}')
        bot.send_message(sender_chat_id, f'Сообщение отправлено{for_people}!')
    except:
        for_people = ''
        if int(receiver_chat_id) == 1337136801:
            for_people = ' Данику'
        elif int(receiver_chat_id) == 1030020149:
            for_people = ' Асану'
        elif int(receiver_chat_id) == 6862396551:
            for_people = ' Насте'
        bot.send_message(sender_chat_id, f'Сообщение{for_people} не отправлено\n'
                                         f'Нет чата с админ версией!')



@bot.message_handler()
def send_error(message):
    bot.send_message(message.chat.id,f'Команда {message.text} не распознана!')

while True:
    start_time = int(time.time())
    print('Admin версия работает!\n')
    msg = ''
    try:
        bot.polling()
    except Exception as e:
        time.sleep(3)
        msg += f'Совершена ошибка ({e})!\n'




    end_time = int(time.time())
    msg += time_refract(start_time, end_time)
    bot.send_message(1337136801, msg)