# 22、函数及python中return的独特之处
def sum_acc(begin, end):
    sum = 0
    acc = 1
    for i in range(begin, end):
        sum += i
        acc *= 1
    return sum, acc

a, b = sum_acc(1, 10)       # 多元赋值
print(f"sum = {a}")
print(f"acc = {b}")

# 23、python选择性接收返回值
_, c = sum_acc(1, 10)   # 用一个"_"就可以实现
print(f"c的取值是{c}")