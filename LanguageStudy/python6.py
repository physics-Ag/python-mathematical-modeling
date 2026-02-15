# 12、python的条件判断及if-else语句三元表达式
a = input("请输入一个整数")
a = int(a)
if a % 2 == 0:
    print("您输入的数是偶数")
else:
    print("您输入的数是奇数")
print("您输入的数是偶数") if a % 2 == 0 else print("您输入的数是奇数")
# 补充：Python中只有False、None、0、0.0、0j、''、[]、()、{}等被认为是False，其他都是True
    
# 13、C/Java/python对于模运算的区别
# 见图片python6.png