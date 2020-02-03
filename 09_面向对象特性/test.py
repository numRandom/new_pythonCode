class Plyer:

    def __init__(self,name):
        self.name = name

class Game:

    def __init__(self,name):
        self.game_name = name

    def start(self,player,game_name):
        print("%s 玩 %s 游戏" % (player,game_name))

player = Plyer("王盼盼")

game = Game("王者荣耀")

game.start(player.name,game.game_name)