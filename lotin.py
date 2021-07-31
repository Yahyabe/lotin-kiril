from transliterate import to_cyrillic, to_latin 
import telebot


TOKEN = '1789725624:AAGR6IgX3AR59WCIEyB-1gAW9lYftrsEkjw'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Xush kelibsiz {0.first_name}!".format(message.from_user, bot.get_me()),parse_mode='html')
    bot.send_message(message.chat.id, "Men  Kiril Lotin Translete qilaman! \nMatn yubor" )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)    
    bot.reply_to(message, javob)


bot.polling()
