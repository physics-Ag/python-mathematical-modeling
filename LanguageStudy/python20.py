# 41、取出所有key和value
a = {
    "student" : 1,
    "teacher" : 2,
    "friend"  : 3
}
print(a.keys())         # 取出所有的key
print(a.values())       # 取出所有的value
print(a.items())        # 取出所有的key value值

# 42、合法的key
# 不是所有的类型都可以设置为key
# 只有不可变类型才可被哈希
print(hash((1, 2, 3)))
# print(hash([1, 2, 3]))    # 这里是不行的，因为[]列表是不可变类型
print(hash(1))
print(hash(True))