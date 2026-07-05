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

# 46、for循环 -- 列表推导式
# 语法：f(i) for i in iterable if condition(i)
a = [1, 2, 3, 4]
# (i * i for i in a)返回的是一个迭代器, 要配合next()才能得到迭代器里面的值 -- 本质是因为惰性求值
b = (i * i for i in a)
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))  # 超出元素会抛出异常
# [i * i for i in a]返回的是已经迭代好的列表 -- 本质是因为[]强迫必须立刻求值
b = [i * i for i in a]
print(b)
b = [i + 5 for i in a]
c = [[i + 5] for i in a]
d = [i for i in a if i % 2 == 0]
print(b)
print(c)
# 上面二者的区别在于，b是一个一维列表，而c是一个二维列表，每个元素都是一个单元素列表
print(d)

# 总结: 无论是map函数还是上面的(f(i) for i in iterable if condition(i)), 其本质都是将可迭代对象进行某种作用, 返回一个迭代器对象, 都采用惰性求值