import sqlite3

from searchkey import searchkey_val
 
conn = sqlite3.connect("dcbotdatabase.db") 
cursor = conn.cursor()
 
# Заполняем таблицу
links = [('111', 'https://www.vkusnyblog.ru/recipe/tvorozhnaya-zapekanka/'),
         ('112', 'https://www.vkusnyblog.ru/recipe/manniki-s-tvorogom/'),
         ('113', 'https://www.vkusnyblog.ru/recipe/blinchiki-s-rikottoj-i-makom/'),
         ('114', 'https://www.vkusnyblog.ru/recipe/syrniki-s-sushenoj-vishnej/'),
         ('115', 'https://www.vkusnyblog.ru/recipe/lenivye-vareniki/')]
 
cursor.executemany("INSERT INTO links VALUES (?,?)", links)
conn.commit()

def result_link():
   print("sql request is started")
   sql = "SELECT link FROM links WHERE key=?"
   cursor.execute(sql, [(str("111"))])
   print(cursor.fetchone()) # or use fetchone()
   return cursor.fetchone()



