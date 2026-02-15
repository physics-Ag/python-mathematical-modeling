# 48、python文件打开与关闭
# 如果不写encoding参数，默认使用系统编码，windows系统默认是gbk编码，linux系统默认是utf-8编码
f = open("test.txt", "w", encoding="utf-8")   # 没有文件则创建文件，有文件则清空文件内容再做写入
f.close()  # 关闭文件，释放资源
f = open("test.txt", "r", encoding="utf-8")   # 读取文件内容，如果没有文件则报错
f.close()  # 关闭文件，释放资源
f = open("test.txt", "a", encoding="utf-8")   # 没有文件则创建文件，有文件则在文件末尾追加内容
f.close()  # 关闭文件，释放资源
# 注意：f是一个文件对象，它会占用资源的，要及时关闭
# w+   读写模式，文件不存在则创建，存在则清空内容
# r+   读写模式，文件不存在则报错，存在则从头开始读写
# a+   读写模式，文件不存在则创建，存在则从末尾开始读写

# 一个案例
# 想说明两点：(1)、不能无限制去打开文件
#            (2)、python有垃圾自动回收机制(GC)，所以当下面的注释代码不被执行时，是可以一直打开文件的，因为python会自动回收资源，即每次循环后会自动关闭文件
num = 0
# a = []
while True:
    f = open("test.txt", "w", encoding="utf-8")
    # a.append(f)
    num += 1
    print(f"第{num}次打开文件")