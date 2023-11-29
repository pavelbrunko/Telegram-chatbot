import telebot
import random

token = '6422195590:AAFt3hIuKm_qJuCVvFkIhVplaCntDj71XJQ'

bot = telebot.TeleBot(token)

HELP = '''
/help - вывести список доступных команд
/add, /todo - добавить задачу в список на определённую дату
/show - напечатать все добавленные задачи на определённую дату
/random - добавить случайную задачу на дату Сегодня'''

RANDOM_TASKS = ['Написать код на Python', 'Закончить продвинутый курс по Python', 'Посмотреть видео по обратному распространению ошибки', 'Вспомнить алгоритмы сортировки']

tasks = dict()

def add_todo(date, task):
    date = date.lower()
    if tasks.get(date) is not None:
        tasks[date].append(task)
    else:
        tasks[date] = [task]

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add', 'todo'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(command=['random'])
def random_add(message):
    date = 'сегодня'
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(commands=['show'])
def show(message):
    date = message.text.split()[1].lower()
    if date in tasks:
        text = ''
        for task in tasks[date]:
            text += f'[ ] {task}\n'
    else:
        text = 'Такой даты нет'
    bot.send_message(message.chat.id, text)

# Постоянно обращается к серверам Телеграм
bot.polling(none_stop=True)