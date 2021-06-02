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

import random

# 定义英雄类timo
class timo:
    hp = 10000  # 血量默认值
    power = 800   # 攻击力默认值

    def __init__(self,hp,power):    # 构造函数，分别把类变量传进来
        self.hp = hp
        self.power = power
        return

    def fight(self,enemy_hp,enemy_power):
        """
        :param enemy_hp: 敌人的血量
        :param enemy_power: 敌人的攻击力
        :return: null
        """
        # 英雄最终的⾎量 = 英雄hp属性-敌⼈的攻击⼒enemy_power
        self.hp = self.hp - enemy_power

        #敌⼈最终的⾎量 = 敌⼈的⾎量enemy_hp - 英雄的power属性
        enemy_hp = enemy_hp - self.power

        if (self.hp > 0) or (enemy_hp > 0):
            if self.hp > enemy_hp:
                print("英雄获胜")
            elif self.hp < enemy_hp:
                print("敌人获胜")
            else:
                print("平局")
        elif self.hp == 0 and enemy_hp == 0:  # 两位英雄的血量同时为0，证明二者的初始血量和攻击力完全一致
            print("平局")
        return

# 定义英雄类police
class police:
    hp = 9000  # 血量默认值
    power = 700  # 攻击力默认值

    def __init__(self,hp,power):
        self.hp = hp
        self.power = power
        return

    def fight(self, enemy_hp, enemy_power):
        """
        :param enemy_hp: 敌人的血量
        :param enemy_power: 敌人的攻击力
        :return: null
        """
        # 英雄最终的⾎量 = 英雄hp属性-敌⼈的攻击⼒enemy_power
        self.hp = self.hp - enemy_power

        # 敌⼈最终的⾎量 = 敌⼈的⾎量enemy_hp - 英雄的power属性
        enemy_hp = enemy_hp - self.power

        if (self.hp > 0) or (enemy_hp > 0) :
            if self.hp > enemy_hp:
                print("英雄获胜")
            elif self.hp < enemy_hp:
                print("敌人获胜")
            else: print("平局")
        elif self.hp == 0 and enemy_hp == 0:  # 两位英雄的血量同时为0，证明二者的初始血量和攻击力完全一致
            print("平局")
        return


def main():
    timo_hp = int(input("请输入timo的初始血量："))
    timo_power = int(input("请输入timo的初始攻击力："))
    police_hp = int(input("请输入police的初始血量："))
    police_power = int(input("请输入police的初始攻击力："))
    CampA = timo(timo_hp,timo_power)
    CampB = police(police_hp,police_power)
    random_key = random.randint(1,2)
    # print(random_key)
    if random_key == 1: # key为1时timo为英雄，police为敌人
        print("本局timo为英雄，police为敌人")
        CampA.fight(CampB.hp,CampB.power)
    elif random_key == 2: # key为2时police为英雄，timo为敌人
        print("本局police为英雄，timo为敌人")
        CampB.fight(CampA.hp, CampA.power)


if __name__ == '__main__':
    main()