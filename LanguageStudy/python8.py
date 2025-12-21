# 16、python生成随机数
# 两个随机10位数相加，答对输出答对，答错什么
import random   # 导入随机模块
a = random.randint(1, 10)   # 左闭右闭
print(f"生成随机数{a}")

# 17、while循环
x = random.randint(1, 10)   # 左闭右闭
y = random.randint(1, 10)   # 左闭右闭
sum = input(f"{x} + {y} = ")
sum = int(sum)
while sum == x + y:
    print("回答正确")
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    sum = input(f"{x} + {y} = ")
    sum = int(sum)