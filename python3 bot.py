# Procfile.windows
import telebot
import config
import random


from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item4 = types.KeyboardButton("⏰ Перемена ⏰")
    item5 = types.KeyboardButton("📋 Расписание 📋")
 
    markup.add(item1, item2, item4, item5)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n Я - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.\n Напиши привет, чтобы узнать больше!!!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 Как дела?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item3 = types.InlineKeyboardButton("Отлично", callback_data='cool')
           
 
            markup.add(item1, item2, item3)
 
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == '⏰ Перемена ⏰':
            bot.send_message(message.chat.id, ("Расписание перемен :\n Урок|   Начало |   Конец |   Длительность перемены\n 1    |    08:30    |  09:15   |   10 минут\n 2    |    09:25    |  10:10   |   20 минут\n 3    |    10:30    |  11:15   |   20 минут\n 4    |    11:35    |  12:20   |   10 минут\n 5    |    12:30    |  13:15   |   10 минут\n 6    |    13:25    |  14:10   |   15 минут\n 7    |    14:25    |  15:10   |   10 минут\n 8    |    15:20    |  16:05   |   00минут "))

        elif message.text == '📋Расписание📋':
            bot.send_message(message.chat.id, ("Выберите день недели:"))

            markup3 = types.InlineKeyboardMarkup(row_width=2)
            pon = types.InlineKeyboardButton('Понедельник:', callback_data='pon')
            wto = types.InlineKeyboardButton('Вторник:', callback_data='wto')
            sre = types.InlineKeyboardButton('Среда:', callback_data='sre')
            che = types.InlineKeyboardButton('Четверг:', callback_data='che')
            pat = types.InlineKeyboardButton('Пятница:', callback_data='pat')

            markup3.add(pon,wto,sre,che,pat)
            bot.send_message(message.chat.id, '======================================', reply_markup=markup3)


           


       
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text.lower() == "пока":
        bot.send_message(message.from_user.id, "Пока создатель!")
          
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == 'cool':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'pon':
                bot.send_message(call.message.chat.id, 'Расписание:\n 1. Биология\n 2. Труд\n 3. История Укр./Харьков\n 4. Алгебра\n 5. Химия\n 6. Немецкий\n 7. Физика ')
            elif call.data == 'wti':
                bot.send_message(call.message.chat.id, 'Расписание:\n 1. Геометрия\n 2. История Укр.\n  3. Укр. Мова\n 4. Инфа\n 5. Английский\n 6. Искусство\n 7. Физ-ра')
            elif call.data == 'sre':
                bot.send_message(call.message.chat.id, 'Расписание:\n 1. Право\n 2. Алгебра\n  3. Укр. Лит\n 4. Химия\n 5. Физика\n 6. Немецкий\n 7. География\n 8. Литература')
            elif call.data == 'che':
                bot.send_message(call.message.chat.id, 'Расписание:\n 1. Русский язык\n 2. Укр.Литература\n 3. Геометрия\n 4. Биология\n 5. Инфа\n 6. Физ-ра\n 7. Литература')
            elif call.data == 'pat':
                bot.send_message(call.message.chat.id, 'Расписание:\n 1. Основы Здоровья\n 2. Всемирная История\n 3. Укр. Мова\n 4. Физ-ра\n 5. Русский язык\n 6. Английский\n 7. Физика\n 8. Классный Час')

        
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
