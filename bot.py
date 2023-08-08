import telebot
from telebot import types
token = '***'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def Bot_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b_start = types.KeyboardButton('Привет')
    markup.add(b_start)
    bot.send_message(message.from_user.id,
                     "Привет, чем я могу тебе помочь?",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def Bot_message(message):
    if message.text == "Привет":
        markup_hello = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b_all_url = types.KeyboardButton('Полезные ссылки')
        b_command = types.KeyboardButton('Команды')
        b_about_me = types.KeyboardButton('Обо мне')
        markup_hello.add(b_all_url, b_command, b_about_me)
        bot.send_message(message.from_user.id,
                         'Чем могу помочь', reply_markup=markup_hello)
    elif message.text == '/about_me' or message.text == 'Обо мне':
        bot.send_message(
            message.from_user.id,
            'Меня зовут Кирилл, мне 21 год\n'
            'Я студент 3 курса по направлени Прикладная информатика в КГЭУ\n'
            'Этого тг бота я сделал для пополнения моего портфолио\n'
            'Ссылку на него и на мой личный тг можно найти с помощью команды /url')
    elif (message.text == "/help"
          or message.text == 'Команды' or message.text == '/command'):
        markup_text = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b_mess_start = types.InlineKeyboardButton('/start')
        b_mess_command = types.InlineKeyboardButton('/command')
        b_mess_url = types.InlineKeyboardButton('/url')
        b_mess_about = types.InlineKeyboardButton('/about_me')
        markup_text.add(b_mess_start, b_mess_command, b_mess_url, b_mess_about)
        bot.send_message(
            message.from_user.id,
            "Список команд:"
            "\n/start - начало общения"
            "\n/command - список команд"
            "\n/url - ссылки на меня"
            '\n/about_me - немного обо мне', reply_markup=markup_text)

    elif message.text == "/url" or message.text == 'Полезные ссылки':
        markup_url = types.InlineKeyboardMarkup()
        b_url_gh = types.InlineKeyboardButton(
            text='GitHub', url='https://github.com/reEch0')
        b_url_tg = types.InlineKeyboardButton(
            text='Telegram', url='https://t.me/reEchoKirill')
        markup_url.add(b_url_gh, b_url_tg)
        bot.send_message(message.from_user.id,
                         "полезные ссылки", reply_markup=markup_url)

    else:
        markup_help = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b_help = types.InlineKeyboardButton('/help')
        markup_help.add(b_help)
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.",
                         reply_markup=markup_help)


bot.polling(none_stop=True, interval=0)
