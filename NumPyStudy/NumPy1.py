import numpy as np

# 1、自定义创建数组
# 这里是通过列表来创建数组
A = np.array([1, 2, 3, 4])
B = np.array([[1, 2, 3, 4], 
              [2, 3, 4, 5], 
              [3, 4, 5, 6]])
print(A)
print(B)
print(type(A))      # 注：我们口头上称呼A是数组，但是我们实际上要知道A的类型是<class 'numpy.ndarray'>，这是NumPy内部自定义的数据结构

# 2、数组的shape
# 返回是一个元组(a, b, ...)，a表示一维下有多少元素，b表示二维下有多少元素，如果行数或者列数为0 ... => 一维就是在第一个方括号内，二维就是在第二个方括号内
print(B.shape)
print(B.shape[0])
print(B.shape[1])

# 3、数组的dtype
# dtype是用于说明数组用什么类型来存储数据，可以自己设置，它是NumPy内部自定义的类型，详见dtype.png => 这也间接说明了数组存储的元素类型是相同的
print(B.dtype)
C = np.array(B, dtype = np.int32)
print(C.dtype)
D = np.array([0.1, 'A', "ABC", 3])      # 如果不指定类型，会选择其中最大类型，即用字符串类型存储
print(D.dtype)