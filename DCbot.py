
#import of components
import logging

from telegram.ext import (CommandHandler, MessageHandler, Updater, Filters, 
                          ConversationHandler)

from telegram import ReplyKeyboardMarkup

from dialog_part_1 import dialog_start, user_temporary_dict

from dialog_part_2 import dialog_part_2, dialog_part_3

from searchkey import searchkey_val

import settings


#логирование в файл
logging.basicConfig(filename='bot.log', level=logging.INFO)


#PROXY settings
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

# Приветствие юзера
def greet_user(update, context):
    
    keyboard_greet = ReplyKeyboardMarkup([
       ['Давай', 'Я передумал']
       ])

    update.message.reply_text(
        f'Привет, не знаешь что приготовить? Понимаю, давай попробую помочь',
        reply_markup = keyboard_greet
        )

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    
    dialog = ConversationHandler( 

        entry_points=[MessageHandler(Filters.regex('^(Давай)$'), dialog_start)],

        states={"user_temporary_dict_meal_type": [MessageHandler(Filters.text,user_temporary_dict)],
                "meal_subtype_selection": [MessageHandler(Filters.text, dialog_part_2)],
                "user_temporary_dict_meal_subtype": [MessageHandler(Filters.text,dialog_part_3)],
                "searchkey_value_for_DB": [MessageHandler(Filters.text,searchkey_val)]
                },

        fallbacks=[]
    )

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(dialog)
    


    # logging.info("Бот стартовал")
    logging.info('Started')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
