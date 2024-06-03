import tkinter as tk
from tkinter import ttk

class Calculator():
    def __init__(self) -> None:
        self.temp_left_num = 0
        self.temp_right_str = "0"
        self.root = tk.Tk()
        self.label = tk.Label(text="電卓")
        self.label.pack()
        self.frame = ttk.Frame(self.root)
        self.frame.grid(column=0, row=0, sticky= tk.NSEW, padx=5, pady=5)
        btn_1 = tk.Button(self.frame, text="1", command=)
        btn_2 = tk.Button(self.frame, text="2",command=)
        btn_3 = tk.Button(self.frame, text="3", command=)
        btn_4 = tk.Button(self.frame, text="4", command=)
        btn_5 = tk.Button(self.frame, text="5", command=)
        btn_6 = tk.Button(self.frame, text="6", command=)
        btn_7 = tk.Button(self.frame, text="7", command=)
        btn_8 = tk.Button(self.frame, text="8", command=)
        btn_9 = tk.Button(self.frame, text="9", command=)
        btn_0 = tk.Button(self.frame, text="0", command=)
        btn_00 = tk.Button(self.frame, text="00", command=)
        btn_addition = tk.Button(self.frame, text="+", command=)
        btn_subtraction = tk.Button(self.frame, text="-", command=)
        btn_multiplication = tk.Button(self.frame, text="x", command=)
        btn_division = tk.Button(self.frame, text="÷", command=)
        btn_equal = tk.Button(self.frame, text="=", command=)
        btn_decimal_point = tk.Button(self.frame, text=".", command=)
        btn_clear_part = tk.Button(self.frame, text="A", command=)
        btn_decimal_point = tk.Button(self.frame, text="AC", command=)
        btn_decimal_point = tk.Button(self.frame, text="+/-", command=)
        btn_decimal_point = tk.Button(self.frame, text="π", command=)
        btn_decimal_point = tk.Button(self.frame, text="!", command=)
        btn_decimal_point = tk.Button(self.frame, text="√", command=)
        btn_decimal_point = tk.Button(self.frame, text="^", command=)


        self.root.mainloop()

    def push_btn_num(self, num: str):
        
    
    def push_btn_plus():
        pass

    def push_btn_plus():
        pass
    



app = Calculator()