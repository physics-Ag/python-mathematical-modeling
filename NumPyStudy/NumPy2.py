import numpy as np

# 4、求矩阵的特征值和特征向量
# 在一定程度上，NumPy库定义的数组就是矩阵
A = np.array([[1, 2, 3, 4], 
              [2, 3, 4, 5], 
              [3, 4, 5, 6], 
              [4, 5, 6, 7]])

# linalg是numpy的线性代数模块，其中的eig方法就是求一个矩阵的特征值和特征向量
eig_val, eig_vec = np.linalg.eig(A)     # eig_val是矩阵的特征值，eig_vec是矩阵的特征向量

# 都是用数组储存的
print(type(eig_val))
print(type(eig_vec))

# 访问方式
# 对于数组的访问，你需要知道下标是从零开始的(和列表差不多)
num = eig_val.shape[0]      # 由于特征值是直接用一行存储的，所以数组eig_val的一维元素个数就是特征值的个数
i = 0
while i != num:
    print(f"{eig_val[i]} 对应的特征向量是 {eig_vec[:, i]}")     # 由于第n列表示第n个特征值所对应的特征向量，eig_vec[:, i]的意思是访问所有行的第i个元素
    i += 1