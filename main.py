import telebot;


bot = telebot.TeleBot('1976365844:AAEzSUgqGfVo3f3fxiQZQb6mpSygxuhv2j8');


@bot.message_handler(content_types=['text'])
def get_text_messages(messege):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True,interval=0)
