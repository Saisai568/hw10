import json  # 未使用的 import

def add(a,b):    # 參數間沒有空格
    result = a+b  # 運算子前後缺空格
    print("計算結果如下：")
    return result  


def  unused_function():   # function 前面多兩個空格
        x = 10            # 過多縮排
        y=20              # 等號前後缺空格
        return x+y        # 未使用的函式（會被視為程式碼異味）

class Test:
    def __init__(self):
        self.value=0       # 等號缺空格

    def calculate(self):
        for i in range(5):
            print(i)

        return self.value

# 多餘空行（會出現 E303）
    
def main():
    add(3,5)

main()  # 缺少 if __name__ == '__main__'
