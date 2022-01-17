
from telegram import ReplyKeyboardMarkup


#определим клавиатуры второго уровня
keyboard_2_lvl_breakfast = ReplyKeyboardMarkup([
        ['Творог'],
        ['Яйца', 'Каша']
        ])

keyboard_2_lvl_soup = ReplyKeyboardMarkup([
        ['Суп-пюре'],
        ['Диетический', 'Сытный']
        ])

keyboard_2_lvl_main = ReplyKeyboardMarkup([
        ['Курица'],
        ['Свинина', 'Говядина']
        ])

keyboard_2_lvl_side = ReplyKeyboardMarkup([
        ['Каши'],
        ['Картофель', 'Овощи'],
        ])


#определим условие выбора клавиатуры 2го уровня
def keyboard_2_lvl_function(update, context):
    user_answer_1_search = context.user_data["dialog_dict"].get("key_part_1")
    
    if user_answer_1_search == "Завтрак":
        update.message.reply_text(
        f"Что больше любишь на завтрак?",
        reply_markup = keyboard_2_lvl_breakfast
        )
        
    elif user_answer_1_search == "Суп":
        update.message.reply_text(
        f"Какой суп предпочитаешь?",
        reply_markup = keyboard_2_lvl_soup
        )

    elif user_answer_1_search == "Основное блюдо":
        update.message.reply_text(
        f"Из чего готовим основное блюдо?",
        reply_markup = keyboard_2_lvl_main
        )
        
    elif user_answer_1_search == "Гарнир":
        update.message.reply_text(
        f"Что выбираешь на гарнир?",
        reply_markup = keyboard_2_lvl_side
        )


