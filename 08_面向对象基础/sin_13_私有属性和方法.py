class Women:

    def __init__(self,name):

        self.name = name
        self.__age = 18

    def secret(self):

        #在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name,self.__age))

xiaofang = Women("小芳")

# 私有属性和私有方法在外界不能被直接访问
# print(xiaofang.__age)

xiaofang.secret()