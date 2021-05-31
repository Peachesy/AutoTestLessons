# 读写文件的操作步骤：
# 1.打开文件，获取文件描述符
# 2.操作文件描述符（读或写）
# 3.关闭文件
# 注：文件读写操作完成后，应及时关闭
# 读取图片的话，格式应为rb


# with语句块执行完毕后会自动关闭文件，所以可以不用再调用close()方法
with open("data.txt",encoding="UTF-8") as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break