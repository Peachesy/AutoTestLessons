# 猜数游戏：
# 计算机出一个1-100之间的随机数由人来猜，
# 计算机根据人猜的数字分别给出“大一点”，“小一点”，“猜对了”
import random

RawNum = random.randint(1,101)
print("RawNum:",RawNum)
# for i in range(101):
#     GuessNum = int(input("请猜数："))
#     if GuessNum > RawNum:
#         print("小一点！")
#     elif GuessNum < RawNum:
#         print("大一点！")
#     else:
#         print("猜对了！")
#         break

while True:
    GuessNum = int(input("请猜数："))
    if GuessNum > RawNum:
        print("小一点！")
    elif GuessNum < RawNum:
        print("大一点！")
    else:
        print("猜对了！")
        break



