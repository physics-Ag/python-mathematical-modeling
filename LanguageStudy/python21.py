# 43、int()和eval()的区别
# int()函数与eval()函数的最大区别在于eval()函数可以解析并执行一个字符串表达式，而int()函数只能将字符串转换为整数
a = eval(input())
b = int(input())
print(a)
print(b)

# 44、字符串的分割函数split()
a = "hello world python"
b = a.split(" ")    # 第一个参数表示分割符，默认为空格；第二个参数表示分割次数，默认为-1，表示分割所有
print(b)    # b是一个列表类型