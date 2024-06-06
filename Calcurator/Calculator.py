import tkinter as tk
from tkinter import ttk
import math

class Calculator():
    def __init__(self) -> None:
        self.temp_left_num: float = None
        self.now_str: str = ""
        self.now_operator: str = None
        self.root = tk.Tk()
        # self.root.geometry("500x400")
        self.frame = ttk.Frame(self.root)
        self.label = tk.Label(self.frame, text=self.now_str)
        self.frame.grid(column=0, row=0, sticky= tk.NSEW, padx=5, pady=5)
        self.update_now_str()
        self.btn_1 = tk.Button(self.frame, text="1", command= lambda: self.push_btn_num("1"))
        btn_2 = tk.Button(self.frame, text="2", command= lambda: self.push_btn_num("2"))
        btn_3 = tk.Button(self.frame, text="3", command= lambda: self.push_btn_num("3"))
        btn_4 = tk.Button(self.frame, text="4", command= lambda: self.push_btn_num("4"))
        btn_5 = tk.Button(self.frame, text="5", command= lambda: self.push_btn_num("5"))
        btn_6 = tk.Button(self.frame, text="6", command= lambda: self.push_btn_num("6"))
        btn_7 = tk.Button(self.frame, text="7", command= lambda: self.push_btn_num("7"))
        btn_8 = tk.Button(self.frame, text="8", command= lambda: self.push_btn_num("8"))
        btn_9 = tk.Button(self.frame, text="9", command= lambda: self.push_btn_num("9"))
        btn_0 = tk.Button(self.frame, text="0", command= lambda: self.push_btn_num("0"))
        btn_00 = tk.Button(self.frame, text="00", command= lambda: self.push_btn_num("00"))
        btn_addition = tk.Button(self.frame, text="+", command= lambda: self.push_btn_operator("+"))
        btn_subtraction = tk.Button(self.frame, text="-", command= lambda: self.push_btn_operator("-"))
        btn_multiplication = tk.Button(self.frame, text="x", command= lambda: self.push_btn_operator("*"))
        btn_division = tk.Button(self.frame, text="÷", command= lambda: self.push_btn_operator("/"))
        btn_equal = tk.Button(self.frame, text="=", command= lambda: self.push_btn_calcutation())
        btn_decimal_point = tk.Button(self.frame, text=".", command= lambda: self.push_btn_num("."))
        btn_clear_part = tk.Button(self.frame, text="A", command= lambda: self.push_btn_clear())
        btn_all_clear= tk.Button(self.frame, text="AC", command= lambda: self.push_btn_all_clear())
        btn_plus_minus = tk.Button(self.frame, text="+/-", command= lambda: self.push_btn_plus_minus())
        btn_pie = tk.Button(self.frame, text="π", command= lambda: self.push_btn_special_operator("π"))
        btn_exclamation_mark = tk.Button(self.frame, text="!", command= lambda: self.push_btn_special_operator("!"))
        btn_root = tk.Button(self.frame, text="√", command= lambda: self.push_btn_special_operator("√"))
        btn_factorial = tk.Button(self.frame, text="^", command= lambda: self.push_btn_operator("^"))

        self.label.grid(column=0, row=0, columnspan=5, sticky=tk.NSEW)
        btn_pie.grid(column=0, row=1)
        btn_exclamation_mark.grid(column=1, row=1)
        btn_root.grid(column=2, row=1)
        btn_factorial.grid(column=3, row=1)
        btn_division.grid(column=4, row=1)
        btn_plus_minus.grid(column=0, row=2)
        btn_7.grid(column=1, row=2)
        btn_8.grid(column=2, row=2)
        btn_9.grid(column=3, row=2)
        btn_multiplication.grid(column=4, row=2)        
        btn_clear_part.grid(column=0, row=3)
        btn_4.grid(column=1, row=3)
        btn_5.grid(column=2, row=3)
        btn_6.grid(column=3, row=3)
        btn_subtraction.grid(column=4, row=3)
        btn_all_clear.grid(column=0, row=4)
        self.btn_1.grid(column=1, row=4)
        btn_2.grid(column=2, row=4)
        btn_3.grid(column=3, row=4)
        btn_addition.grid(column=4, row=4, rowspan=2, sticky=tk.NSEW)
        btn_0.grid(column=0, row=5)
        btn_00.grid(column=1, row=5)
        btn_decimal_point.grid(column=2, row=5)
        btn_equal.grid(column=3, row=5)
        
        print("temp_left_num: {},\nnow_str: {},\nnow_operator: {}\n".format(self.temp_left_num, self.now_str, self.now_operator))
        self.root.mainloop()

    # 数値に変換可能かの確認
    def is_number(self, num_str: str):
        if(num_str == "." and len(self.now_str) == 0):
            num_str = "0."
        try:
            float(self.now_str + num_str)
        except ValueError:
            return False
        else:
            return True

    # 頭に.が来た際の処理, 0の処理　必要
    def push_btn_num(self, num_str: str):
        # 数字処理できるか判定
        if(self.is_number(num_str)):
            self.now_str = self.now_str + num_str
            self.update_now_str()
        
        print("{}_btn_was_pushed.\n".format(num_str))

    def push_btn_operator(self, next_operator: str):
        if(self.temp_left_num and self.now_operator):
            if(self.now_operator == "+"):
                self.temp_left_num = self.temp_left_num + float(self.now_str)
                self.now_operator = next_operator
            elif(self.now_operator == "-"):
                self.temp_left_num = self.temp_left_num - float(self.now_str)
                self.now_operator = next_operator
            elif(self.now_operator == "*"):
                self.temp_left_num = self.temp_left_num * float(self.now_str)
                self.now_operator = next_operator
            elif(self.now_operator == "/"):
                self.temp_left_num = self.temp_left_num / float(self.now_str)
                self.now_operator = next_operator
            elif(self.now_operator == "^"):
                self.temp_left_num = self.temp_left_num ** float(self.now_str)
                self.now_operator = next_operator
        elif(self.now_operator == None and self.now_str == ""):
            pass
        else:
            self.temp_left_num = float(self.now_str)
            self.now_operator = next_operator
        self.push_btn_clear()
        self.show_temp()

    
    def push_btn_special_operator(self, special_operator: str):
        if(special_operator == "π"):
            self.now_str = str(float(self.now_str) * math.pi)
        elif(special_operator == "!"):
            pass
            self.now_str = str(math.factorial(float(self.now_str)))
        elif(special_operator == "√"):
            pass
            self.now_str = str(math.sqrt(float(self.now_str)))
        self.update_now_str()

    def push_btn_calcutation(self):
        self.push_btn_operator(None)
        print("temp_left_num: {},\nnow_str: {},\nnow_operator: {}\n".format(self.temp_left_num, self.now_str, self.now_operator))
        self.show_temp()


    def push_btn_clear(self) -> None:
        if(self.now_str != ""):
            self.now_str = ""
        elif(self.now_str == ""):
            self.push_btn_all_clear()
        self.update_now_str()
        self.show_temp()

    def push_btn_all_clear(self) -> None:
        self.temp_left_num = None
        self.now_str = ""
        self.now_operator = None
        self.update_now_str()

    def show_temp(self):
        self.label.configure(text=self.temp_left_num)

    # 引数の値を更新する　ここで数値に直して計算したい
    def update_now_str(self):
        self.label.configure(text= self.now_str)
        print("temp_left_num: {},\nnow_str: {},\nnow_operator: {}\n".format(self.temp_left_num, self.now_str, self.now_operator))
        
    # 初期にー入れた場合はどうする？
    def push_btn_plus_minus(self):
        if(len(self.now_str) == 0):
            pass
        elif(self.now_str[0] != "-"):
            self.now_str = "-" + self.now_str
        else:
            self.now_str = self.now_str[1:]
        self.update_now_str()

app = Calculator()