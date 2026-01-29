# 45、map函数
# map函数用于将一个指定的函数作用于给定序列（如列表、元组等）中的每个元素，并返回一个迭代器（map对象）
# Python的迭代器采用惰性求值的方式，这意味着只有在需要时才会计算每个元素，所以map函数不会立即执行，而是返回一个可迭代的map对象
# 可以使用list()函数将map对象转换为列表，从而获取所有处理后的结果
# 语法：map(function, iterable, ...)
# (1)、只涉及一个对象
a = [1, 2, 3, 4, 5]
b = map(lambda x: x**2, a)   # map函数将a中的每个元素传递给lambda函数进行处理，返回一个map对象
print(list(b))    # 将map对象转换为列表并打印结果
# (2)、涉及多个对象
c = [10, 20, 30, 40, 50]
d = map(lambda x, y: x + y, a, c)  # map函数将a和c中的对应元素传递给lambda函数进行处理
print(list(d))    # 将map对象转换为列表并打印结果

# 46、列表推导式
# 简单来说就是迭代器中每个元素都去执行一次表达式，然后把结果收集到一个新的列表中
# 语法：[expression for item in iterable if condition]
a = [1, 2, 3, 4, 5]
b = [i + 5 for i in a]
c = [[i + 5] for i in a]
d = [i for i in a if i % 2 == 0]
print(b)
print(c)
# 上面二者的区别在于，b是一个一维列表，而c是一个二维列表，每个元素都是一个单元素列表
print(d)