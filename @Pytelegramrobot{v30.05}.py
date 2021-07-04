import telebot
from telebot import types
import time
#@{LiderKoder}
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('/start','/tezlik') 
markup.row('Salom') 
#@infoPyTelebot | @phpdevelopersuz
bot = telebot.TeleBot("1857494087:AAGEa2A7RJnhjWV_UTIre-t383rPtJfHiio", parse_mode='html')

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "<b>Assalomu alaykum\nUshbu bot pytelegrambotapi kutubxonasi orqalik yaratilmoqda\nBuyruqlar: <code>/tezlik</code> - Bot tezligi, <code>Salom</code> - Assalomu alaykum\n\nYangiliklar @phpdevelopersuz kanalida :)</b>", reply_markup=markup)

@bot.message_handler(commands=['tezlik'])
def start(message):
    millisec = round(time.time() * 1000)
    send = bot.send_message(message.chat.id, "Bot tezligi: 0 ms")
    current = round(time.time() * 1000) - millisec
    xabar = "<b>Bot tezligi: </b>" + str(current) + " ms"
    bot.edit_message_text(text=xabar, chat_id=message.chat.id, message_id=send.message_id)
    
@bot.message_handler(content_types=['text'])
def text(message):
	if message.text == "Salom":
		bot.send_message(message.chat.id,"Assalomu alaykum",reply_markup=markup)
		
bot.polling(none_stop=True)

#Bot yangiliklari :👇
#@infoPyTelebot | @phpdevelopersuz
#Obuna bolamiz :)