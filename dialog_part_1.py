
from telegram import ReplyKeyboardMarkup

#определим клавиатуру первого уровня
keyboard_1_lvl = ReplyKeyboardMarkup([
        ['Завтрак', 'Суп'],
        ['Основное блюдо', 'Гарнир']
        ])

def dialog_start(update, context):
    print("dialog started")
    update.message.reply_text(
        f'Теперь попробуем уточнить детали.',
        reply_markup = keyboard_1_lvl
        )
    print("dialog started2")
    return "user_temporary_dict_meal_type"

def user_temporary_dict(update, context):
    print("user temp dict started")
    user_answer_1 = update.message.text
    context.user_data["dialog_dict"] = {"key_part_1": user_answer_1}
    print(context.user_data)
    return "meal_subtype_selection"
