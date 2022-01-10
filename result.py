from searchkey import searchkey_val

#определим функцию подбора результирующей ссылки для пользователя
def result_link (update, context):
    update.message.reply_text(
        searchkey_val
        )