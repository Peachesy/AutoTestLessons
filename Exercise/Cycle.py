# 1. 计算1-100求和
# 2. 加入分支结构实现1-100之间的偶数求和
# 3. 使用python实现1-100之间的偶数求和

# 1. 计算1-100求和
res = 0
for i in range(1,101):
    res = res+i
print("Ans1:",res)

# 2. 加入分支结构实现1-100之间的偶数求和
n = range(1,101)
res = 0
for i in n:
    if i%2 ==0:
        res = res+i
print("Ans2:",res)

# 3. 使用python实现1-100之间的偶数求和
res = 0
for i in range(0,101,2):
    print(i)
    res = res+i
print("Ans3:",res)
