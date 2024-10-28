import telebot

token = "7232733132:AAFrBzPdnBPaDdSm6VL9WclHvrub1sr8eAg"
bot = telebot.TeleBot(token)

#---------------------------------------------------------------------------
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

# Запуск бота -------------------------------------------------------------
bot.polling()
