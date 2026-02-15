# 55、字符串乘法
b = "666 \n" * 10
print(b)

# 56、print的格式化对齐打印(f"{}")
# 左对齐
print(f"{'Text':<10}")  # 'Text      ' 类似C语言的printf("%-10s", "Text");
# 右对齐
print(f"{'Text':>10}")  # '      Text' 类似C语言的printf("%10s", "Text");
# 居中对齐
print(f"{'Text':^10}")  # '   Text   '
# 带填充字符
print(f"{'Text':*^10}")  # '***Text***'