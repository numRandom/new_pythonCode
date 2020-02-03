class Animal:
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")

class Dog(Animal):

    def bark(self):
        print("汪汪汪叫")


class XiaoTianQuan(Dog):

    def bark(self):
        print("神一样的叫唤……")

    def fly(self):
        print("我会飞")

# 1、创建一个哮天犬的对象
xtq = XiaoTianQuan()

xtq.bark()
xtq.fly()