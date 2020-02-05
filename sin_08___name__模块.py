# 全局变量、函数、类，直接执行的代码不是向外界提供的工具！
def say_hello():
    print("你好你好~")

if __name__ =="__main__":
    print(__name__)

    # 文件导入时，能够直接执行的代码不需要被执行
    print("小明创建")
    say_hello()