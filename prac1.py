import re

class Practice1:
    def __init__(self) -> None:
        pass

    def re_base_num(self, input_str) -> list:
        if(input_str == "help"):
            print("""スコアに入力可能な文字は, 「数字(0-9)」, 「カンマ(,)」, 「半角スペース」のみ「カンマ(,)」は数値の区切り文字とする""")
            return self.re_base_num(input("Input >"))
        # elif(input_str == r"[- ,]"):
        #     print("指定文字以外が含まれています.\n再度入力して下さい.\n")
        #     return re_base_score(input_score())
        else:
            # 空白をまず消し、その後数字を取得する(,区切りで数字を見るため "2 2"を2,2と取りたい場合は.replaceを削除)
            # "3 -5"がはじけない現状だと[3,-5]となってしまうため
            num_array = re.findall(r"-?\d+", input_str.replace(" ", ""))
            print("入力値: {}".format(num_array))
            # 指定文字以外の配列を作る
            str_array = re.findall(r"[^0-9^,^ ^-]", input_str)
            if(0 < len(re.findall(r"[^0-9^,^ ^-]", input_str))):
                print("指定文字以外が含まれています.\n再度入力して下さい.\n")
                return self.re_base_num(input("Input >"))
            if(0 < len(re.findall(r'\b\d+\-\d+\b', input_str))):
                print("計算分を入れないでください.\n再度入力してください.\n")
                return self.re_base_num(input("Input >"))
            if(len(num_array) <= 0):
                # ↓入力が"-"のみの場合「空白です」に入ってしまう...
                print("空白です.\n再度入力してください.\n")
                return self.re_base_num(input("Input >"))
            else:
                for score in num_array:
                    if(int(score) <= 0):
                        print("0以下の値が含まれます.\n再度入力してください.\n")
                        return self.re_base_num(input("Input >"))
                return num_array
            
    def sort_list(self, list_str: list) -> list:
        result = []
        for str_num in list_str:
            result.append(int(str_num))
        print("数値返還: {}".format(result))
        result.sort() 
        print("数値ソート: {}".format(result))
        return result
    
class Practice2:
    def __init__(self) -> None:
        pass

    def fizz_buzz(self, start_num: str, end_num:str) -> None:
        for i in range(end_num-start_num+1):
            if((i+start_num) % 3 == 0 and (i+start_num) % 5 == 0):
                print("FizzBuzz, ")
            elif((i+start_num) % 3 == 0):
                print("Fizz, ")
            elif((i+start_num) % 5 == 0):
                print("Buzz, ")
            else:
                print("{}, ".format(i+start_num))


def main() -> None:
    # p1_class = Practice1()
    # list_num = p1_class.re_base_num(input("Input >"))
    # print("Output >{}".format(p1_class.sort_list(list_num)))
    
    p2_class = Practice2()
    p2_class.fizz_buzz(-2,35)


if __name__ == "__main__":
    main()