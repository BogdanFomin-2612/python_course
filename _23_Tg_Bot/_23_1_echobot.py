from telebot import TeleBot

TOKEN = "8887547522:AAGPUuSaTDnOqrGDxpsphzeOA_NGUhJDPLw"

bot = TeleBot(TOKEN)        #? Инициализация Бота

@bot.message_handler(commands=["start", "help"])        #? 
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)

bot.infinity_polling()