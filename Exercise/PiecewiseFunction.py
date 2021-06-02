# 分段函数求值：
# 3x-5(x>1)
# f(x)=x+2(-1<=x<=1)
# 5x+3(x<-1)
# 分别使用分支嵌套以及多重分支实现分段函数求值

# 嵌套层次多了之后会影响代码的可读性，所以扁平化的代码编写更好些，即多重分支的写法

x=int(input("请输入x的值："))

# 分支嵌套
# x = int(input("请输入x的值："))
if x>1:
    res = x*3-5
else:
    if x>=-1:
        res = x+2
    else:
        res = x*5+3
print("嵌套分支的结果：",res)

# 多重分支
# x=int(input("请输入x的值："))
if x>1:
    res=x*3-5
elif -1<=x<=1:
    res=x+2
else:
    res=x*5+3
print("多重分支的结果：",res)

