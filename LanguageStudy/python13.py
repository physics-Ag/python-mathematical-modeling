# 26、关键字参数
def test(x, y):
    print(f"x = {x}", end = " ")
    print(f"y = {y}")

test(x = 10, y = 20)
test(y = 100, x = 200)
# 形如上述 test(x=10, y=20) 这样的操作, 即为 关键字参数

# 27、len函数求字符串长度
a = input("请输入字符串")   # 由于input默认接收的就是str类型，所以后面不需要进行类型转换
print(f"字符串的长度是:{len(a)}")
