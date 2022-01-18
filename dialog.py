
from telegram import ReplyKeyboardMarkup

from telegram.ext.conversationhandler import ConversationHandler

from keyboards import keyboard_2_lvl_function

from searchkey import searchkey_val

#определим клавиатуру первого уровня
keyboard_1_lvl = ReplyKeyboardMarkup([
        ['Завтрак', 'Суп'],
        ['Основное блюдо', 'Гарнир']
        ])

def dialog_start(update, context):
    print("dialog started")
    update.message.reply_text(
        f'Уточни, пожалуйста, что ты хочешь приготовить?.',
        reply_markup = keyboard_1_lvl
        )
    return "meal_subtype_selection"

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