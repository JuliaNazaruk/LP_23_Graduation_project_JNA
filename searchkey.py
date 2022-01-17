
from random import randint
from telegram.ext.conversationhandler import ConversationHandler

#определим ключ для поиска ссылки для отправки пользователю по следующему правилу:
# где первая часть ключа - это параметр первого уровня, вторая часть ключа - это параметр второго уровня, 
# а третья часть - это случайное число в заданном диапазоне


#словарь для определения значения первого праметра ключа
key_part1_dictionary = {
    "Завтрак":"1",
    "Суп":"2",
    "Основное блюдо":"3",
    "Гарнир":"4"
}


#определим первый параметр ключа
def key_part1_def(update, context):
    user_answer_1 = context.user_data["dialog_dict"].get("key_part_1")
    key_part1 = key_part1_dictionary[user_answer_1]
    print (key_part1)
    return key_part1
    

#словарь для определения значения второго праметра ключа
key_part2_dictionary = {
    "Творог":"1",
    "Яйца":"2",
    "Каша":"3",
    "Пюре":"1",        
    "Диетический":"2",
    "Сытный":"3",
    "Курица":"1",        
    "Свинина":"2",
    "Говядина":"3",      
    "Каши":"1",        
    "Картофель":"2",
    "Овощи":"3" 
}


#определим второй параметр ключа
def key_part2_def(update, context):
    user_answer_2 = context.user_data["dialog_dict"].get("key_part_2")
    print(user_answer_2)
    key_part2 = key_part2_dictionary[user_answer_2]
    print (key_part2)  
    return key_part2


#определим третий параметр ключа - случайное число в диапазоне от 1 до 5
def key_part3_def(number):
    key_part3 = randint(1, 5)
    return key_part3


#"соберем" весь ключ
def searchkey_val(update, context):
    print ("searchkey_val started")
    print (key_part2_def)
    full_key = str(key_part1_def)&str(key_part2_def)&str(key_part3_def)
    print (full_key)
    
    return ConversationHandler.END


