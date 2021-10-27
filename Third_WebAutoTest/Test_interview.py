import random

num_list = [9,8,1,5,-5]
# print(type(num_list[2]))


# for j in num_list:
#     if j >= 0:
#



temp = 0
max_num = 0
# for i in range(0,5):
for j in num_list:
    temp = temp + j
    if temp >= max_num:
        max_num = temp
    else:
        max_num = max_num

print(max_num)
