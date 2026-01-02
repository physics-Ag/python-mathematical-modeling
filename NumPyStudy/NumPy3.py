import numpy as np

# 5、np.max函数和max函数的区别
# 对于max函数输出什么类型取决于里面放什么，放NumPy里面的东西，就是NumPy内部定义的类型
#                            放入的是列表，就是列表元素对应的类型
# 对于np.max函数输出无论里面是什么，输出的都是NumPy内部定义的类型
A = np.array([1, 2, 3, 4])
B = [1, 2, 3, 4]
print(type(np.max(A)))
print(type(max(A)))
print(type(max(B)))
print(type(np.max(B)))
# 总结：使用NumPy库里面的东西，返回或者使用的类型都是NumPy里面的类型

# 6、np.max函数和np.argmax函数
A = np.array([[1, 2, 3, 4], [2, 3, 4, 5]])
print(np.max(A))            # 返回最大值
print(np.argmax(A))         # 返回最大元素对应的索引值，多维数组会被展开，下标从0开始
print(np.argmax(A, axis = 0))         # 返回每一行的最大索引值，多维数组会被展开，下标从0开始
print(np.argmax(A, axis = 1))         # 返回每一列的最大索引值，多维数组会被展开，下标从0开始