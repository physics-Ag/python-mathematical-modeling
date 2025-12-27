# 39、字典的增删查
a = {   # 左边是key，右边是key对应的值
    "student" : 1,
    "teacher" : 2,
    "friend"  : 3
}
# (1)、查
# a、使用 in 可以判定 key 是否在 字典 中存在. 返回布尔值
print("student" in a)
# b、使用[]通过类似于取下标的方式, 获取到元素的值. 只不过此处的 "下标" 是 key
print(a["friend"])      # 如果key不存在，这里会直接抛异常
# (2)、增/改
a["go"] = 4             # 增
a["friend"] = "0"       # 改
print(a)
# (3)、删
a.pop("student")        # pop(key)表示删除key
print(a)

# 40、字典的遍历
for key in a:           # 注意返回的是键值，而非键对值
    print(key, a[key])