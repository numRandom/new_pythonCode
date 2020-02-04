def input_password():

    # 1、提示用户输入密码
    psw = input("请输入密码：")

    # 2、判断用户密码长度 >= 8，返回用户输入的密码
    if len(psw) >= 8:
        return psw

    # 3、如果 < 8, 主动抛出异常
    # 1> 创建一个 Exception 对象
    ex = Exception("密码长度不够 8 位")

    # 2> 主动抛出异常对象
    raise ex

try:
    print(input_password())
except Exception as result:
    print(result)