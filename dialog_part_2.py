from telegram.ext.conversationhandler import ConversationHandler

from keyboards import keyboard_2_lvl_function


def dialog_part_2(update, context):
    print("dialog_part_2_activated")
    keyboard_2_lvl_function (update, context)
    
    return "user_temporary_dict_meal_subtype"

def dialog_part_3(update, context):
    print("dialog_part_3_activated")
    user_answer_2 = update.message.text
    context.user_data["dialog_dict"] = {"key_part_2": user_answer_2}
    print(context.user_data)
    return "searchkey_value_for_DB"