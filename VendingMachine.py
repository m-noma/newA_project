import mysql.connector as db

import tkinter as tk
from tkinter import ttk

class VendingMachineDB:
    def __init__(self) -> None:
        self.my_db = db.connect(host = "localhost", user = "root", password="", db = "vending_machine_db")
        self.my_db.ping(reconnect=True)
        print("is connected?: {}\n".format(self.my_db.is_connected()))
        self.cursor = self.my_db.cursor(buffered=True)

    # クエリ実行
    def execute_the_query(self, query: str) -> None:
        try:
            self.cursor.execute(query)
            self.my_db.commit()
        except Exception as err:
            print(f"Error: '{err}'")

    # 表示 未実装
    def show_table(self, query: str) -> list:
        result: list = []
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            if data != None:
                for d in data:
                    result.append(d)
            print(result)
        except Exception as err:
            print(f"Error: {err}")

    # 削除時実行
    def __del__(self) -> None:
        self.cursor.close()
        self.my_db.close()
        print("database was closed.\n")

class VendingMachineUI:
    def __init__(self, product_list) -> None:
        self.root = tk.Tk()
        self.frame = ttk.Frame(self.root)
        self.label = tk.Label(self.frame, text="おはようございます")
        self.frame.grid(column=0, row=0, sticky= tk.NSEW, padx=5, pady=5)   
        # ここの処理を自動化させたい  
        # self.text_product_0:str = None
        # btn_product_0 = tk.Button(self.frame, text=self.text_product_0, command= lambda: self.push_btn_product(0))
        # self.text_product_1:str = None
        # btn_product_1 = tk.Button(self.frame, text=self.text_product_1, command= lambda: self.push_btn_product(1))
        # self.text_product_2:str = None
        # btn_product_2 = tk.Button(self.frame, text=self.text_product_2, command= lambda: self.push_btn_product(2))
        # self.text_product_3:str = None
        # btn_product_3 = tk.Button(self.frame, text=self.text_product_3, command= lambda: self.push_btn_product(3))
        # self.text_product_4:str = None
        # btn_product_4 = tk.Button(self.frame, text=self.text_product_4, command= lambda: self.push_btn_product(4))
        # ここまで
        for i, product in product_list:
            locals()["btn_" + ]

        self.label.grid(column=0, row=0, columnspan=5, sticky=tk.NSEW)




    def push_btn_product(self, btn_num: int):
        if(btn_num == 0):
            pass

my_db = VendingMachineDB()
# print(my_db.execute_the_query())

my_db.show_table("SELECT * FROM `product_tb`;")
del my_db
    