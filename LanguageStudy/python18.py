# 37、元组
a = (1, 2, 3, 4, 5)
b = tuple(a)            # tuple()括号里面放的是同为元组的变量
c = (1, 2, 3, 4, 5)
d = (1, 2, 3, 4)
# 由于元组是不可变类型，当值相同时，会指向相同
print(a is b)
print(a is c)
print(a is d)
# 元组除了不能增删外，其余操作和列表是一样的

# 38、字典的创建
a = {
    "student" : 1,
    "teacher" : 2,
    "friend"  : 3
}
b = dict(a)             # dict()括号里面放的是同为字典的变量
c = a
print(a is b)           # 说明dict()创建的是一个新对象
print(a is c)