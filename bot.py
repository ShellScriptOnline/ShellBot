import telebot

bot = telebot.TeleBot('1331803384:AAEda1KF8KzLXSQZWbC8VvzTI9CLEhjKZS4')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Что это за бот?', 'Скрипт 4.8 CPM')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Это тестовый бот написаный на Python от SHELL Car Parking', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'что это за бот?':
        bot.send_message(message.chat.id, 'Это тестовый бот написаный на Python от SHELL Car Parking')
    elif message.text.lower() == 'скрипт 4.8 cpm':
        bot.send_message(message.chat.id, '--------------------------------------------------------\n--------------------------------------------------------\nДобавлен "Спид-Хак 2.0"\nДобавлен "Хром на машины где слетает яркость"\n--------------------------------------------------------\n--------------------------------------------------------\nhttps://oxy.st/d/bhcc')


bot.polling()