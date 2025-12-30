import numpy as np

# 1、自定义创建矩阵 -- 这里都以矩阵来称呼数组
# 这里是通过列表来创建矩阵
A = np.array([1, 2, 3, 4])
B = np.array([[1, 2, 3, 4], 
              [2, 3, 4, 5], 
              [3, 4, 5, 6]])
print(A)
print(B)

# 2、数组的shape
# 返回是一个元组(a, b)，a表示行数，b表示列数，如果行数或者列数为0，就不要通过下标去访问！！
print(B.shape)
print(B.shape[0])
print(B.shape[1])

# 3、数组的dtype
# dtype是用于说明矩阵数据类型的对象
print(B.dtype)
C = np.array([0.1, 'A', "ABC", 3])      # 都会提升类型，提升为字符串存储
print(C.dtype)