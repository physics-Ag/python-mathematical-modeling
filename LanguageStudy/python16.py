# 32、python赋值对于所有类型都是引用，只是在修改的时候会因类型是否可变而产生差别
# 对于int, float, str, 元组, bool类型都是不可变类型，它们会因为值的修改而改变指向
# 对于自定义类型、列表、字典都是可变类型，它们不会因为修改而改变指向
# 编译器优化：对于不可变类型，当值相同时，会指向相同
# (1)、bool类型
a = True; b = True; c = False
print(a is b, end = " ")
b = False
print(b is c)
# (2)、int类型
a = 10; b = a; c = 10
print(a is c, end = " ")
print(a is b, end = " ")
a = 20
print(a is b)
# (3)、str类型
a = "abcd"; b = "abcd"; c = a
print(a is b,  end = " ")
print(a is c, end = " ")
c = "ccccc"
print(a is c)
# (4)、元组
a = (1, 2, 3); b = (1, 2, 3); c = a
print(a is b,  end = " ")
print(a is c, end = " ")
c = (1, 2)
print(a is c)
# 可变类型
a = [1, 2, 3]; b = a; c = [1, 2, 3]
print(a is b,  end = " ")
print(a is c, end = " ")
b.append(4)
print(a is b)

# 33、list()和=创建列表的区别
# list()表示创建一个值相同的新对象给对方引用
# =表示同时引用
a = [1, 2, 3, 4]; b = list(a); c = a
print(a is b, end = " ")
print(a is c, end = " ")