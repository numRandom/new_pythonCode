def demo(*args,**kwargs):

    print(args)
    print(kwargs)

args = (1,2,3,4,5,6)
kwargs = {"name":"王盼盼","age":18,"sex":"female"}

# 多值函数的错误传递
# demo(args,kwargs)
# 正确传递，拆包语法，简化元组变量 / 字典变量的传递
demo(*args,**kwargs)