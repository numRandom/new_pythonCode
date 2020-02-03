class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1,self.__num2))

class B(A):

    def demo(self):

        # 1、在子类方法中，不能访问父类的私有属性
        print("访问父类的私有属性 %d" % self.__num2)
        # 2、在子类方法中，不能调用父类的私有方法
        self.__test()

# 1、创建一个子类对象
b = B()
print(b)

# 在外界不能直接访问对象的私有属性 / 调用私有方法
print(b.num1)
# b.__test()