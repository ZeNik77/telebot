import telebot
from xd import TOKEN
from os import path
import pprint

token = TOKEN

bot = telebot.TeleBot(token)

file_name = path.join(path.dirname(__file__), F)

users = set()
@bot.message_handler(commands=['start'])
def start(message):
    global users
    with open('users.txt', 'r') as f:
        users = set([el[:-1] for el in f.readlines()])
        print(users)
    with open('users.txt', 'a') as f:
        if str(message.chat.id) not in users:
            f.write(str(message.chat.id)+'\n')


    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('ИНФА'), telebot.types.KeyboardButton('ПОЛУЧИТЬ КФГ'))
    bot.send_message(message.chat.id, 'лол я тут', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def say(message):
    if message.text == 'ИНФА':
        bot.send_message(message.chat.id, 'бот который халявно выдает vpn')
    elif message.text == 'ПОЛУЧИТЬ КФГ':
        with open(file_name, 'rb') as f:
            bot.send_document(message.chat.id, f)



@bot.message_handler(content_types=['document'])
def document(message):
    if message.chat.id == 916776182:
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            src = message.document.file_name
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)

        except Exception as e:
            print(e)

    else:
        bot.send_message(message.chat.id, 'лол зачем мне файл ты чего')


bot.polling(none_stop=True)
