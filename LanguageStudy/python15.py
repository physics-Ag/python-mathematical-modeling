# 30、使用 len 函数可以获取到列表的元素个数
a = [1, "666", 0.987]
print(len(a))
# 所以 => [-1] 相当于 a[len(a) - 1]

# 31、python中==和is的区别
# python中的==是判断数据是否相同，is判断是否是同一个对象
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a
print(a is b)
print(a == b)
print(a is c)
print(a == c)