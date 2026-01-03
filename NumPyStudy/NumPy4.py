import numpy as np

def show(a, b, c):
    print(a)
    print(b)
    print(c)

# 7、np.sum函数、np.prod函数、np.power函数
A = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])

a = np.sum(A)
b = np.sum(A, axis = 0)
c = np.sum(A, axis = 1)
show(a, b, c)

a = np.prod(A)
b = np.prod(A, axis = 0)
c = np.prod(A, axis = 1)
show(a, b, c)

a = np.power(A)
b = np.power(A, axis = 0)
c = np.power(A, axis = 1)
show(a, b, c)