import telebot
from transliterate import to_cyrillic, to_latin


TOKEN = "5192078807:AAEkshAh4Iv2uZKho1Qtt_yERAdfBL5gkqM"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalom aleykum, Translit botimizga Xush kelibsiz!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	xabar = message.text
	javob = lambda xabar: to_cyrillic(xabar) if xabar.isascii() else to_latin(xabar)
	bot.reply_to(message, javob(xabar))

bot.infinity_polling()
