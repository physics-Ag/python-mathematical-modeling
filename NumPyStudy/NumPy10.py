import numpy as np

# 17、指数函数与对数函数
x = np.array([1, 2, 3, 4])
print(np.exp(x))    # e的指数函数
# print(np.exp3(x))   # 这个个函数不存在，无法计算以3为底的指数函数，可以使用np.power(3, x)来计算以3为底的指数函数
print(np.log(x))    # 以e为底对数
print(np.log10(x))  # 以10为底的对数
print(np.log2(x))   # 以2为底的对数
# print(np.log3(x))   # 这个个函数不存在，无法计算以3为底的对数，可以使用np.log(x) / np.log(3)来计算以3为底的对数

# 18、全一列和全一行
data = np.array([[1, 2, 3, 4, 5], 
             [2, 3, 4, 5, 6]])
print(np.ones((len(data), 1)))           # 全1列
print(np.ones((1, len(data[0]))))        # 全1行

# 19、列合并函数与行合并函数
a = np.c_[data, np.ones((len(data), 1))]    # 列合并函数
print(a)
b = np.r_[data, np.ones((1, len(data[0])))] # 行合并函数
print(b)
# 补充：len(a)表示a的行数，len(a[0])表示a的列数