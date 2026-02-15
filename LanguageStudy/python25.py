import sys

def func(name, age, city):
    print(f"姓名：{name}，年龄：{age}，城市：{city}")

# 50、**解包字典
# 解包字典相当于从 :, 变成 =, 并且去掉了{}
a = {"name": "赵锦辉", "age": 18, "city": "北京"}
print(a)
# a **= a # 这种写法是错误的，**= 是幂运算的赋值运算符，不能用于字典
# 用法一：函数参数传递
func(**a)  # 等价于 func(name="赵锦辉", age=18, city="北京")
# 用法二：合并字典
b = {"name": "李华", "age": 20, "sex": "男"}
c = {**a, **b}  # 合并字典，后面的键值对会覆盖前面的
print(c)

# 51、python程序退出
sys.exit(0)                         # 退出码式的退出(给父进程看)
exit("content")                     # 退出并在屏幕上显示消息, 等价于quit()
quit("content")                     # 退出并在屏幕上显示消息, 等价于exit()
# Jupyter看不到exit()和quit()的退出消息的原因：内核捕获到这个退出请求后, 立即关闭内核(相当于杀掉进程, 所有变量全部消失), 退出消息可能被丢弃或来不及显示