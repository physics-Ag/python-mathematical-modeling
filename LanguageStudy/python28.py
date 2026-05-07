# 57、函数装饰器
# (1)、定义装饰函数
def decorate(func):     # 对于外层装饰函数, 函数参数必须是被装饰函数
    def wrapper(x):     # 定义内层装饰函数, 函数参数必须是需要被装饰的函数的参数
        print("hello world", end=" ")
        print(func(x))  # 调用原函数并传入原函数所需参数x(非必须)
    return wrapper      # 返回内层装饰函数

# 使用装饰函数方法一
@decorate
def func1(a):
    return a

# 使用装饰函数方法二
def func2(a):
    return a
func3 = decorate(func2)

func1(10)  # 输出: hello world 10
func3(10)  # 输出: hello world 10