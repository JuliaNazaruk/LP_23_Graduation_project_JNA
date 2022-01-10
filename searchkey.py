
from random import randint


#определим ключ для поиска ссылки для отправки пользователю по следующему правилу:
# где первая часть ключа - это параметр первого уровня, вторая часть ключа - это параметр второго уровня, 
# а третья часть - это случайное число в заданном диапазоне

def searchkey_val(update, context):
    full_key = str(key_part1_def)&str(key_part2_def)&str(key_part3_def)
    return full_key


#определим первый параметр ключа
def key_part1_def(update, context):
    user_answer_1 = update.message.text
    key_part1 = ""
    if user_answer_1 == "Завтрак":
        key_part1 = "1"
        
    elif user_answer_1 == "Суп":
        key_part1 = "2"

    elif user_answer_1 == "Основное блюдо":
        key_part1 = "3"
        
    elif user_answer_1 == "Гарнир":
        key_part1 = "4"
    
    return key_part1


#определим второй параметр ключа
def key_part2_def(update, context):
    user_answer_2 = update.message.text
    key_part2 = ""
    if user_answer_2 == "Творог":
        key_part2 = "1"
        
    elif user_answer_2 == "Яйца":
        key_part2 = "2"

    elif user_answer_2 == "Каша":
        key_part2 = "3"
      
    elif user_answer_2 == "Пюре":
        key_part2 = "1"
        
    elif user_answer_2 == "Диетический":
        key_part2 = "2"

    elif user_answer_2 == "Сытный":
        key_part2 = "3"

    elif user_answer_2 == "Курица":
        key_part2 = "1"
        
    elif user_answer_2 == "Свинина":
        key_part2 = "2"

    elif user_answer_2 == "Говядина":
        key_part2 = "3"
      
    elif user_answer_2 == "Каши":
        key_part2 = "1"
        
    elif user_answer_2 == "Картофель":
        key_part2 = "2"

    elif user_answer_2 == "Овощи":
        key_part2 = "3"        
   
    return key_part2


#определим третий параметр ключа - случайное число в диапазоне от 1 до 5
def key_part3_def(number):
    key_part3 = randint(1, 5)
    return key_part3


print (searchkey_val)