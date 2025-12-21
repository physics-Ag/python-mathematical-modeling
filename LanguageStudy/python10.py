# 20、pass空语句
a = 1
b = 2
if a == b:
    # 这个代码块是必须写内容的，但是实际上你又感觉不需要写，可以用pass代替
    pass
else:
    print("a和b不相等")
    
# 21、continue和break
# 打印所有的1到10中的所有偶数
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i, end = " ")
print()
# 求任意数量的数的和，以分号结尾
sum = 0
print("请输入求和数，以分号结尾:")
while True:
    x = input()     # 没输入一个数要按下回车键
    if x == ";":
        break
    sum += int(x)
print(f"sum = {sum}")