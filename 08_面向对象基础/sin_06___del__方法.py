class Cat:

    def __init__(self,new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 走啦" % self.name)

# Tom 是一个全局变量
tom = Cat("Tom")
print(tom.name)

del tom

print("+" * 50)
