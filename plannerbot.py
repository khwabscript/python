import telebot

commands_list = """
		Оля, вот, что я могу:
		/help - список команд
		/add - добавить дело
		/del - удалить дело
		/view - что еще осталось
		"""
TOKEN = "1492623618:AAGFcPyCSrfGbUjqwrW7KH-ZQjymTdNNkAY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, commands_list)
	

@bot.message_handler(commands=['view'])
def view_deal(message):
	text_file = open('test.txt', 'r', encoding = 'UTF-8')
	lines = text_file.readlines()
	text_file.close()
	if len(lines) > 1:
		bot.send_message(message.chat.id, ''.join(lines))
	else:
		bot.send_message(message.chat.id, "Список дел пуст!")	

@bot.message_handler(commands=['add'])
def question_add(message):
	bot.send_message(message.chat.id, "Что хотите добавить?")
	# @bot.message_handler(content_types=['text'])
	@bot.message_handler(regexp='\w*\D+\w*')
	
	def add_deal(message):
		text_file = open('test.txt', 'a+', encoding = 'UTF-8')
		deal = message.text + '\n'
		text_file.write(deal)
		text_file.close()
		bot.send_message(message.chat.id, "Добавлено:)") 
	

	
@bot.message_handler(commands=['del'])
def question_del(message):
	bot.send_message(message.chat.id, "Что хотите удалить?")
	bot.send_message(message.chat.id, "Вот, что у Вас есть:")
	view_deal(message)
	# @bot.message_handler(content_types=['text'])
	@bot.message_handler(regexp='\d+')

	def del_deal(message):
		text_file = open('test.txt', 'r', encoding = 'UTF-8')
		lines = text_file.readlines()
		text_file.close()
		try:
			if lines[int(message.text)] in lines:
			    del lines[int(message.text)]
			text_file = open("test.txt", "w", encoding = 'utf-8')
			x = ''.join(lines)
			text_file.write(x)
			text_file.close()
			bot.send_message(message.chat.id, "Готово!") 
		except:
			send_welcome(message)


bot.polling()
