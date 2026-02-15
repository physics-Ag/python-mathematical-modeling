# 48、python文件的读和写
f = open("test.txt", "w", encoding="utf-8")
f.write("Hello\nGood\nBad\nGreat\nWorld\n")
f.close()
f = open("test.txt", "r", encoding="utf-8")
# 读法1：
content = f.read()
print(content)
# 读法2：
f.seek(0)  # 将文件指针移动到文件开头，因为前面已经读过了
content = f.readlines()  # 读取所有行，返回一个列表
print(content)
# 读法3：
f.seek(0)  # 将文件指针移动到文件开头，因为前面已经读过了
for line in f:
    print(line)
# 拓展：读写文件 和 在终端上显示是有区别的，读写文件C/C++/java/python都是要考虑编码问题的
# 但是在终端上显示时，只有C/C++需要考虑编码问题，java和python在终端上显示时会自动处理编码问题(因为在系统上封装一层解释器解决了这个问题)
    
# 49、文件上下文管理器
# 使用with语句可以自动管理文件的打开和关闭
# 当你离开with块时，文件会自动关闭，有点像智能指针
with open("test.txt", "r", encoding="utf-8") as f:
    # 文件操作
    print()