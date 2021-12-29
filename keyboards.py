
from telegram import ReplyKeyboardMarkup


#определим клавиатуру первого уровня
keyboard_1_lvl = ReplyKeyboardMarkup([
        ['Завтрак', 'Суп'],
        ['Основное блюдо', 'Гарнир']
        ])


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
    user_answer_1 = update.message.text
   
    if user_answer_1 == "Завтрак":
        update.message.reply_text(
        f"Что больше любишь на завтрак?",
        reply_markup = keyboard_2_lvl_breakfast
        )
        
    elif user_answer_1 == "Суп":
        update.message.reply_text(
        f"Какой суп предпочитаешь?",
        reply_markup = keyboard_2_lvl_soup
        )

    elif user_answer_1 == "Основное блюдо":
        update.message.reply_text(
        f"Из чего готовим основное блюдо?",
        reply_markup = keyboard_2_lvl_main
        )
        
    elif user_answer_1 == "Гарнир":
        update.message.reply_text(
        f"Что выбираешь на гарнир?",
        reply_markup = keyboard_2_lvl_side
        )


