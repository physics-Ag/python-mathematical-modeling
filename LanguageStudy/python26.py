# 52、字符串方法：startswith()和endswith()判断字符串首尾
# startswith()：判断字符串是否以指定的子字符串开头，返回True或False
# endswith()：判断字符串是否以指定的子字符串结尾，返回True或False
print("test.cpp".endswith('.cpp'))
print("test.cpp".endswith('.c'))
print("test.cpp".startswith('test'))
print("tset.cpp".startswith('test'))

# 53、内置函数：all()和any()判断元素的真假
# all()：判断可迭代对象中的所有元素是否都为真，如果是，返回True；如果有一个元素为假，返回False
# any()：判断可迭代对象中的元素是否至少有一个为真，如果是，返回True；如果所有元素都为假，返回False
# print(any(["", False]))
# print(any(["", "", True]))
# print(all(["", False]))
# print(all(["hello", True]))

# 54、成员运算符：in和not in判断元素是否在序列中
# in：判断元素是否在序列中，如果在，返回True；如果不在，返回False
# not in：判断元素是否不在序列中，如果不在，返回True；如果在，返回False
print(10 in [1, 2, 3, 4, 5])
print("acm" in "join in acm")
print("acm" not in "join in acm")