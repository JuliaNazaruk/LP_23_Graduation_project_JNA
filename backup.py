#import of components
import logging

from telegram.ext import (CommandHandler, MessageHandler, Updater, Filters, 
                          ConversationHandler)

from dialog_part_1 import dialog_start

from dialog_part_2 import dialog_part_2, dialog_part_3

from result import result_link

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
        entry_points=[CommandHandler("start", dialog_start)],

        states={"key_part_1": [MessageHandler(Filters.text, dialog_part_2)],
                "key_part_2": [MessageHandler(Filters.text, dialog_part_3)]},

        fallbacks=[]
    )

    dp.add_handler(dialog)
    dp.add_handler(MessageHandler(Filters.text, result_link))

    # logging.info("Бот стартовал")
    logging.info('Started')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()





