import mysql.connector as db

my_db = db.connect(
            host = "localhost",
            user = "root",
            password="",
            db = "vending_machine_db"
        )
# print(my_db)
my_db.ping(reconnect=True)
print(my_db.is_connected())
print()
cur = my_db.cursor()
cur.execute("INSERT INTO `vending_machine_db`.`product_tb` VALUE (6, 'ちんこ', 110, 10);")
