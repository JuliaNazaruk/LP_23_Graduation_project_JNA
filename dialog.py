
from telegram import ReplyKeyboardMarkup

from telegram.ext.conversationhandler import ConversationHandler

from keyboards import keyboard_2_lvl_function

from searchkey import searchkey_val

# Приветствие юзера
def greet_user(update, context):
    
    keyboard_greet = ReplyKeyboardMarkup([
       ['Давай', 'Я передумал']
       ])

    update.message.reply_text(
        f'Не знаешь что приготовить? Понимаю, давай попробую помочь',
        reply_markup = keyboard_greet
        )


#определим клавиатуру первого уровня
keyboard_1_lvl = ReplyKeyboardMarkup([
        ['Завтрак', 'Суп'],
        ['Основное блюдо', 'Гарнир']
        ])

#начало диалога с пользователем - выбор основного типа еды
def dialog_start(update, context):
    print("dialog started")
    update.message.reply_text(
        f'Уточни, пожалуйста, что ты хочешь приготовить?',
        reply_markup = keyboard_1_lvl
        )
    return "meal_subtype_selection"

#второй уровень выбора - уточнение деталей
def dialog_part_2(update, context):
    print("dialog_part_2_activated")
    user_answer_1 = update.message.text
    context.user_data["dialog_dict1"] = {"key_part_1": user_answer_1}
    print(context.user_data)
    print("dialog_part_2_keyboard_activated")
    keyboard_2_lvl_function (update, context)
    return "user_temporary_dict_meal_subtype"

#определение результирующей ссылки и прощание
def dialog_part_3(update, context):
    print("dialog_part_3_activated")
    user_answer_2 = update.message.text
    context.user_data["dialog_dict2"] = {"key_part_2": user_answer_2}
    print(context.user_data)
    searchkey_val(update, context)
    print("link is started")
    update.message.reply_text(searchkey_val(update, context)) 
    keyboard_bye = ReplyKeyboardMarkup([
       ["/start"]
       ])

    update.message.reply_text(
        f'Могу найти еще один рецепт - нажми /start',
        reply_markup = keyboard_bye
        )
    return ConversationHandler.END

#диалог после нажатия кнопки "Я передумал"
def user_changed_his_mind(update, context):
    
    keyboard_bye = ReplyKeyboardMarkup([
       ["/start"]
       ])

    update.message.reply_text(
        f'Ничего страшного, я подожду тут. Если понадобится моя помощь - нажми /start и я найду рецепт для тебя',
        reply_markup = keyboard_bye
        )