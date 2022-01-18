
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


#"соберем" весь ключ
def searchkey_val(update, context):
    print ("searchkey_val started")
    user_answer_1 = context.user_data["dialog_dict1"].get("key_part_1")
    print("user_answer_1",user_answer_1)
    key_part1 = key_part1_dictionary[user_answer_1]
    print("key part 1",key_part1)
    print(type(key_part1))
    user_answer_2 = context.user_data["dialog_dict2"].get("key_part_2")
    print("user answer 2",user_answer_2)
    key_part2 = key_part2_dictionary[user_answer_2]
    print("key part 2", key_part2)
    key_part3 = str(randint(1, 5))
    print("random", key_part3)
    full_key = "".join ([key_part1,key_part2,key_part3])
    print ("full key",full_key)
    


