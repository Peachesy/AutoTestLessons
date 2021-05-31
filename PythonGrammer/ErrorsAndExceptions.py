
try:
    num1 = int(input("请输入一个除数"))
    num2 = int(input("请输入一个被除数"))
    print(num1/num2)
# except:
#     print("通用型异常")
except ZeroDivisionError:
    print("被除数不能为0!!!")
except ValueError:
    print("被除数不能为字符型数据！！！！")
finally:
    print("无论程序是否有异常都会执行该语句块")


# 自定义异常通常用raise方法