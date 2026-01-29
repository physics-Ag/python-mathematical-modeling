# 18、for循环及print函数不换行写法
for i in range(1, 10):      # i是循环变量，range(1, 10)是可迭代对象，range是左闭右开区间
    print(i, end = " ")
print()
# 如果是range(num)，表示从0开始，到num-1结束的一个左闭右开区间
    
# 19、range的步长
j = input("请输入步长:")
j = int(j)
for i in range(1, 10, j):   # range(begin, end, step)第三个参数不写默认是1，range在一开始就固定了，后续是无法更改的！
    print(i, end = " ")
    j += 1                  # 这里改变j，但range已经固定了