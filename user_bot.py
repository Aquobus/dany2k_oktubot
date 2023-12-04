import time
import telebot

import user_functions as UF

ADMIN_TOKEN = '6150086911:AAF4_c3-dvd2c78uQ6ZNA7oYf8FMg1u5HjI'

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
    start_msg = UF.uf_start(message)
    msg = start_msg[0]
    if len(start_msg) == 2:
        bot.send_message(1337136801, start_msg[1])
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['cmd1'])
def cmd1(message):
    cmd1_return = UF.uf_who_is_on_duty(message)
    bot.send_message(message.chat.id, cmd1_return)

@bot.message_handler(commands=['cmd2'])
def cmd2(message):
    cmd2_return = UF.uf_my_info(message)
    bot.send_message(message.chat.id, cmd2_return)

@bot.message_handler(commands=['cmd3'])
def cmd3(message):
    cmd3_return = UF.instruct(message)
    bot.send_message(message.chat.id, cmd3_return)


@bot.message_handler()
def send_error(message):
    bot.send_message(message.chat.id,f'Команда {message.text} не распознана!')


while True:
    start_time = int(time.time())
    print('Пользовательская версия работает!\n')
    msg = ''
    try:
        bot.polling()
    except Exception as e:
        time.sleep(3)
        msg += f'Совершена ошибка ({e})!\n'

    end_time = int(time.time())
    msg += time_refract(start_time, end_time)
    bot.send_message(1337136801, msg)
