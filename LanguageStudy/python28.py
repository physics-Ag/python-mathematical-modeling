# 57、函数装饰器
# (1)、定义装饰函数
def decorate(func):     # 对于外层装饰函数, 函数参数必须是被装饰函数
    def wrapper(x):     # 定义内层装饰函数, 函数参数必须是需要被装饰的函数的参数
        print("hello world", end=" ")
        print(func(x))  # 调用原函数并传入原函数所需参数x(非必须)
    return wrapper      # 返回内层装饰函数, 事实上, 也可以返回类(前提是你要在外层装饰函数里面定义内层装饰类)

# 使用装饰函数方法一
# 进行完这次操作, 这个func1函数就等于装饰函数里面return的类或者函数
@decorate
def func1(a):
    return a

# 使用装饰函数方法二
def func2(a):
    return a
func3 = decorate(func2)

func1(10)  # 输出: hello world 10
func3(10)  # 输出: hello world 10

# 58、python类的self参数和函数调用
class Dog:
    def __init__(self):
        print("__init__")

    def fun1():
        print("func1()")
    def fun2(self):
        print("func2()")

# 1、对于Dog(), 首先会创建Dog实例, 然后通过实例调用__init__, 再返回实例, 所以__init__(self)里的self必须写!
dog1 = Dog()

Dog.fun1()
# Dog.fun2()    # 这是不行的!因为self参数没被接收
# dog1.fun1()   # 这是不行的!因为会转化为Dog.fun1(dog1), 但是fun1函数不接受dog1参数
dog1.fun2()

# 59、python没有函数重载