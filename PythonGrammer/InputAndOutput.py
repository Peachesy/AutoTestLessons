# 字面量--以变量或常量给出的原始数据，在程序中可以直接使用
# 三种使用方法
# 1.格式化输出
# 2.string.format()
# 3.Formatted string literal, 字符串格式化机制

name = "Katty Perry"
age = 18
salary = 10009873.930759

namelist = ["katty perry","Harry Potter","Ron",'Tom Riddle']
genderdict ={"katty perry":"famale","Harry Potter":"male","Ron":"male","Tom Riddle":"male"}

# 1.格式化输出

print("Name is %s" % name)
print("Age is %d" % age)
print("Name is %s,age is %d" % (name,age))

# 2.string.format()
print("Name is {},age is {},salary is {}".format(name,age,salary))
# {}里的数字0,1,2代表后面format方法中的变量值，在这种情景中，{0}为name,{1}为age,{2}为salary
print("Name is {0},age is {1},salary is {2}".format(name,age,salary))
print("Name is {2},age is {0},salary is {1}".format(name,age,salary))
print("Name is {2},age is {0},salary is {1}，{1}{2}{0}{1}".format(name,age,salary))

# 列表和字典也可以通过该方式使用，若需访问到每个元素，则直接执行解包操作即可
# 列表的解包用*，字典的解包用**
print("Names are {}".format(namelist))
print("Gender is {}".format(genderdict))

print("Names are {},{},{}".format(*namelist))
print("Gender is {},{}".format(*genderdict))  #这个时候拿到的是key值而不是value
print("Gender is {Harry Potter}，{Ron}".format(**genderdict))  #这个时候拿到的才是key对应的value

# 3.Formatted string literal, 字符串格式化机制
# 使用方法：f{变量名}
# {}里可以是表达式或函数，但不能转义，不能使用“\”
# 列表和字典也不需要解包

print(f"Names are {namelist}")
print(f"My favorite name is {namelist[2]},the gender is {genderdict['Ron']}")
print(f"Name is {name.upper()}")
print(f"lambda {(lambda x:x+1)(2)}")  # 注：如果表达式中需要加冒号，必须将该表达式用括号括起来
print(f"里面也可以放{'常量'}")

