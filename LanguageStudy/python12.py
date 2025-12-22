# 24、python中的变量作用域
def test():
    x = 1

x = 2
if x == 1:
    a = 1
    print(f"x的取值是1")
elif x == 2:
    a = 2
    print(f"x的取值是2")
else:
    a = x
    print(f"x的取值是{x}")

print(f"在if中定义的a在if外也能访问, a = {a}")
# 总结：在python中，只有在函数和类中定义的变量会存在一个独立的作用域，其余定义的变量都在存在于全局域的
#       查找一个变量，先看当前在什么作用域，在全局域就只会在全局域中去寻找；在局部域就先会在当前局部域中查找，再在全局域中查找

# 25、python的函数可以设置参数默认值
def test(x = 10):
    print(x)

test()
test(5)