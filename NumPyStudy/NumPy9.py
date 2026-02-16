import numpy as np

# 14、sqrt()函数
# (1)、计算单个元素的平方根
a = 16
print(np.sqrt(a))
# (2)、计算数组中每个元素的平方根
print(np.sqrt([[1, 4, 9, 16], 
              [36, 4, 64, 100]]))


# 15、tile()函数
# 第一个参数表示要复制的数组，第二个参数表示对应维度复制的次数
# (a, b, c, ...)，从左往右开始表示第0维、第1维、第2维、...的复制次数，先复制第0维，再复制第1维，依次类推 =>与广播类似，广播也是用低维去补高维
A = np.array([0, 1, 2])
print(np.tile(A, 2))
print(np.tile(A, (2, 1)))
print(np.tile(A, (3, 2)))
print(np.tile(A, (3, 2, 3)))

# 16、arange()函数
# 类似于Python内置的range()函数，但返回的是数组
# 左闭右开区间，默认步长为1
print(np.arange(5))          # 从0开始，到5结束，步长为1
print(np.arange(5, 10))      # 从5开始，到10结束，步长为1
print(np.arange(5, 10, 2))   # 从5开始，到10结束，步长为2