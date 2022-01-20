
#import of components
import logging

from telegram.ext import (CommandHandler, MessageHandler, Updater, Filters, 
                          ConversationHandler)

from telegram import ReplyKeyboardMarkup, update

from dialog import greet_user, dialog_start, dialog_part_2, dialog_part_3, user_changed_his_mind

import settings


#логирование в файл
logging.basicConfig(filename='bot.log', level=logging.INFO)


#PROXY settings
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    
    dialog = ConversationHandler( 

        entry_points=[MessageHandler(Filters.regex('^(Давай)$'), dialog_start)],

        states={"meal_subtype_selection": [MessageHandler(Filters.text, dialog_part_2)],
                "user_temporary_dict_meal_subtype": [MessageHandler(Filters.text,dialog_part_3)],
                },

        fallbacks=[]
    )

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(dialog)
    dp.add_handler(MessageHandler(Filters.regex('^(Я передумал)$'), user_changed_his_mind))
    

    # logging.info("Бот стартовал")
    logging.info('Started')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
