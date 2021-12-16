
#import of components
import logging

from telegram.ext import CommandHandler, MessageHandler, Updater

from telegram import ReplyKeyboardMarkup

import settings

#логирование в файл
logging.basicConfig(filename='bot.log', level=logging.INFO)

#PROXY settings
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

# Приветствие юзера
def greet_user(update, context):
    
    keyboard_1_lvl = ReplyKeyboardMarkup([
        ['Завтрак', 'Суп'],
        ['Основное блюдо', 'Гарнир'],
        ['Рулетка']
        ])

    update.message.reply_text(
        f'Привет, не знаешь что приготовить? Понимаю, давай попробуем уточнить детали. Если подойдет совершенно любая идея - выбирай рулетку ;)',
        reply_markup = keyboard_1_lvl 
        )

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    # logging.info("Бот стартовал")
    logging.info('Started')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
