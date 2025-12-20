# 8、not and or -> 同C/C++/java一样也会有短路
a = 10
b = 20; c = 30      # 另类的写法，这个时候才需要加上分号，其余情况都不需要
print(b > a and a > c)
print(b > a > c)    # 等价于上面那种写法
print(b > a or a > c)
print(not b > a)

# 9、多元赋值和链式赋值
a = b = 10
print(a)
print(b)
c = 20
a, c = c, a         # 实现了a与c之间变量值的交换
print(a)
print(c)