class Dog:

    # 不需要传递第一个参数
    # 不访问实例属性 / 类属性
    @staticmethod
    def run():

        print("小狗快跑……")

# 通过类名. 调用静态方法 —— 不需要创建对象
Dog.run()