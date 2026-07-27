# 70、强制关键字参数分隔符 -- "*"
def add_node(self, node: str, action: str, *, defer: bool, metadata: str):
    ...
# *本身不是一个参数, 它是一个分隔符, 表示之后的所有参数都必须用关键字方式传递, 不能按位置传递

# 71、接收任意关键字参数 -- "**"
def add_node(self, **kwargs):
    ...
# **kwargs的含义是: 收集所有未匹配的关键字参数, 打包成一个字典, 字典的名字叫做kwargs

# 72、两个相邻字符串会自动合并
# 注意换行时必须加括号
a = ("123"
"234"
"789")
print(a)
