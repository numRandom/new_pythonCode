# 全局变量
num = 10

def demo():

    # 修改全局变量，使用 global 声明一下变量
    global num
    num = 99

    print("demo ==> %d" % num)

print("函数前的全局变量 num = %d" % num)

demo()

print("函数后的全局变量 num = %d" % num)