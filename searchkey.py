
from random import randint
from telegram.ext.conversationhandler import ConversationHandler
from dictionaries import key_part1_dictionary, key_part2_dictionary, search_result

#определим ключ для поиска ссылки для отправки пользователю по следующему правилу:
# где первая и вторая часть ключа - это параметр соответствующий выбору из первой и второй клавиатуры соответственно, 
# а третья часть - это случайное число в заданном диапазоне от 1 до 5


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
    result_link_to_send=search_result.get(full_key)
    print (result_link_to_send)
    return result_link_to_send



    


