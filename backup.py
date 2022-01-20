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





#DIALOG PART 2
from telegram.ext.conversationhandler import ConversationHandler

from keyboards import keyboard_2_lvl_function

from searchkey import searchkey_val


def dialog_part_2(update, context):
    print("dialog_part_2_activated")
    user_answer_1 = update.message.text
    context.user_data["dialog_dict1"] = {"key_part_1": user_answer_1}
    print(context.user_data)
    print("dialog_part_2_keyboard_activated")
    keyboard_2_lvl_function (update, context)
    return "user_temporary_dict_meal_subtype"

def dialog_part_3(update, context):
    print("dialog_part_3_activated")
    user_answer_2 = update.message.text
    context.user_data["dialog_dict2"] = {"key_part_2": user_answer_2}
    print(context.user_data)
    searchkey_val(update, context)
    print(searchkey_val())
    return ConversationHandler.END


#return cursor.fetchone()