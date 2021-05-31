"""
⼀个回合制游戏，有两个英雄，分别以两个类进⾏定义。分别是timo和police。每个英雄都有 hp 属性和 power属性，hp 代表⾎量，power 代表攻击⼒
每个英雄都有⼀个 fight ⽅法， fight ⽅法需要传⼊“enemy_hp”（敌⼈的⾎量），“enemy_power”（敌⼈的攻击⼒）两个参数。
英雄最终的⾎量 = 英雄hp属性-敌⼈的攻击⼒enemy_power
敌⼈最终的⾎量 = 敌⼈的⾎量enemy_hp-英雄的power属性
即为：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
英雄最终的⾎量和敌⼈最终的⾎量 ，两个 hp 进⾏对⽐，⾎量剩余多的⼈获胜。
如果英雄赢了打印 “英雄获胜”，如果敌⼈赢了，打印“敌⼈获胜”
"""
# 定义敌人类
class timo:
    hp = 10000  # 代表血量
    power = 800   # 代表攻击力

    def __init__(self,hp,power):    # 构造函数，分别把类变量传进来
        self.hp = hp
        self.power = power
        return

    def fight(self,enemy_hp,enemy_power):
        my_hp = self.hp - enemy_hp
        """
        :param enemy_hp:
        :param enemy_power:
        :return:
        """
        return

# 定义英雄类
class police:
    hp = 9000
    power = 700

    def __init__(self):
        return

    def fight(self, enemy_hp, enemy_power):
        """
        :param enemy_hp:
        :param enemy_power:
        :return:
        """
        return


def main():
    # my_hp =
    # my_power =
    return

if __name__ == '__main__':
    main()