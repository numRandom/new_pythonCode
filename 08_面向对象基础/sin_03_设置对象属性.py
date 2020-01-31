class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self接收哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("小猫爱喝水")

# 创建猫对象
tom = Cat()

# 在类外边可以使用 .属性名，给对象定义一个属性
tom.name = "Tom"

tom.eat()
tom.drink()

# 在创建一个猫对象
lazy_cat = Cat()

lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()

print(tom)
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)
