# 14、在Python中使用缩进表示代码块
a = 10
if a > 10:
    print("11111")
    print("22222")
else:
    if (a > 9):
        print("33333")
        print("44444")
    else:
        print("55555")
    print("66666")
print("77777")

# 15、判断闰年的代码(a:int中的int只是类型提示，不一定是a真正的类型)
a:int = input("请输入年份:")
a = int(a)
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(f"{a}是闰年")
else:
    print(f"{a}不是闰年")