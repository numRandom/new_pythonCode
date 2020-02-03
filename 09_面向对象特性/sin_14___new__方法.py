class MusicPlayer:

    # 一个 * 表示多值的元组参数
    # 两个 ** 表示多值的字典参数
    def __new__(cls,*args,**kwargs):

        # 1、创建对象时，new 方法会被自动调用
        # 方法被重写时，父类的 __new__ 方法不会执行
        print("创建对象，分配空间")

        # 2.1、为对象分配空间
        # instance = super().__new__(cls)
        #
        # # 2.2、返回对象的引用
        # return instance

    def __init__(self):
        print("播放器初始化")

# 创建播放器对象
player = MusicPlayer()

print(player)