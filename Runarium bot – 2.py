import telebot
import os
import json
import random
import re
from dotenv import load_dotenv




load_dotenv()  
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)


#------Декоратор----------------------------------------------------

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Виконується функція: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функція {func.__name__} виконана")
        return result
    return wrapper
    
#-------------------------------------------------------------------



# Обробник команди /start
@bot.message_handler(commands=['start'])
@decorator
def send_welcome(message):
    bot.send_message(message.chat.id, "Вітаю! Я бот Рунарій, створений для того щоб допомогти вам в запам'ятовуванні рун. \n\n Щоб дізнатись необхіну інформацію використайте команду /info. \n\n Також майте на увазі що у мене немає серверів які б підримували мене в робочому стані, тому якщо ви хочете скористатись мною - напишіть моєму творцю @Yokoshimaslav")


# Обробник команди /info
@bot.message_handler(commands=['info'])
@decorator
def send_welcome(message):
    bot.send_message(message.chat.id, ' При використані бота майте на увазі що він ще на дуже "сирих" стадіях, і функціонує досить обмежено і незручно. \n\n Поки що в бота є три режими: \n 1) /Run_Name - бот дає вам руну, а ви маєте написати її назву. \n 2) /Name_Run - бот дає вам назву руни, а ви повинні відправити відповідний символ. \n 3) /Run_Meaning - бот дає вам руну, а ви повинні написати її значення (наприклад: Захист, Дар, тощо). \n\n також бот може видати вам набір символів, якщо потрібно (/get_elder_futhark). \n\n Якщо є якісь пропозиції, зауваження, тощо - пишіть @Yokoshimaslav')


# Обробник команди /get_elder_futhark
@bot.message_handler(commands=['get_elder_futhark'])
@decorator
def send_welcome(message):
    bot.send_message(message.chat.id, 'Руни старшого футарку для копіювання: \n\n ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ  ᚷ ᚹ     ᚺ ᚾ ᛁ ᛃ ᛇ ᛈ ᛉ ᛋ      ᛏ ᛒ ᛖ ᛗ ᛚ ᛜ ᛝ ᛞ')


# Шлях до папки з картками Elder_Futhark ----------------------------------------------------------
cards_folder = 'C:/Games/Python/Runariumbot/Elder_Futhark'
#------------------------------------------------------------------------------------------------


# Функція для вибору випадкової карточки з папки -----------------------------------------------------
def get_random_card():
    files = [f for f in os.listdir(cards_folder) if f.endswith('.json')]
    random_file = random.choice(files)
    with open(os.path.join(cards_folder, random_file), 'r', encoding='utf-8') as f:
        card = json.load(f)
    return card
# -----------------------------------------------------------------------------------------------------



#-------------------------Перший Блок-----------------------------------------------------------------

# Обробник команди /Run_Name -------------------------------------------------------------------------
@bot.message_handler(commands=['Run_Name'])
def run_name_quiz(message):
    card = get_random_card()
    rune = card['rune']
    correct_answers = [card['name'], card['Lat.name'], card['Run.name']]
    
    # Відправлення руни з запитанням
    bot.send_message(message.chat.id, f"{rune} - як називається ця руна?")
    
    # Зберігаємо правильні відповіді
    bot.register_next_step_handler(message, check_answer, correct_answers)

# Функція перевірки відповіді
def check_answer(message, correct_answers):
    user_answer = message.text.strip()
    if user_answer in correct_answers:
        bot.send_message(message.chat.id, "ви вгадали")
    else:
        bot.send_message(message.chat.id, "ви помилились")

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------



#-----------------Другий Блок---------------------------------------------------------------------

# Обробник команди -----------------------------------------------------------------------------
@bot.message_handler(commands=['Name_Run'])
def run_quiz(message):
    card = get_random_card()
    rune = card['rune']
    options = [card['name'], card['Lat.name'], card['Run.name']]
    
    # Випадковий вибір назви
    question_name = random.choice(options)
    
    # Відправка назви руни з запитанням
    bot.send_message(message.chat.id, f"{question_name} - яка відповідна руна?")
    
    # Зберігання правильного символу
    bot.register_next_step_handler(message, check_rune_answer, rune)

# Функція перевірки відповіді
def check_rune_answer(message, correct_rune):
    user_answer = message.text.strip()
    if user_answer == correct_rune:
        bot.send_message(message.chat.id, "ви вгадали")
    else:
        bot.send_message(message.chat.id, "ви помилились")
#--------------------------------------------------------------------------------------



#------------------Третій Блок---------------------------------------------------------
 
# Обробник команди --------------------------------------------------------------------
@bot.message_handler(commands=['Run_Meaning'])
def run_meaning_quiz(message):
    card = get_random_card()  
    rune = card['rune']
    meaning = card['meaning']
    
    # Відправляємо руну з запитанням ----------------------------------------------------
    bot.send_message(message.chat.id, f"{rune} - що символізує ця руна?")
    
    # Зберігаємо правильне значення
    bot.register_next_step_handler(message, check_meaning_answer, meaning)

# Функція перевірки відповіді -------------------------------------------------------------
def check_meaning_answer(message, correct_meaning):
    user_answer = message.text.strip().lower()  # Приведення до нижнього регістру для порівняння
    keywords = extract_keywords(correct_meaning)  # Виділення ключових слів із значення
    
    if any(keyword in user_answer for keyword in keywords):
        bot.send_message(message.chat.id, "ви вгадали")
    else:
         correct_answers = ', '.join(keywords)
         bot.send_message(message.chat.id, f"ви помилились. Правильні відповіді: {correct_answers}")

# Функція для виділення ключових слів зі значення ---------------------------------------------
def extract_keywords(meaning):
    # Видалення "Руна символізує:" і поділ тексту на слова
    clean_meaning = re.sub(r"[^\w\s]", "", meaning)  # Видаляє пунктуацію
    words = clean_meaning.lower().split()
    
    # Видаляє слова які не мають значення
    ignore_words = {"руна", "символізує"}
    keywords = [word for word in words if word not in ignore_words]
    
    return keywords

#-----------------------------------------------------------------------------------------------------------

# Запуск бота
bot.polling(none_stop=True)