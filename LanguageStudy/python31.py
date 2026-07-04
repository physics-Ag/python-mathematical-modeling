from typing import Optional
from pydantic import Field

# 65、python说明类成员的属性的方法
# 注: (Optional[str]) 等价于 (str | none)
class test:
    # 下面的self.name无法说明, 只能强制定义
    # 注: Field这种等号只适合于这种场合
    name: Optional[str] = Field(default=None, description="这个人的名字")
    def __init__(self):
        self.name = "123"

# 66、set数据类型(集合类型)
# set类型的定义方法:
# (1)、使用set()函数
print(type(set([1, 1, 2, 2, 3, 3])))
print(type(set({1, 1, 2, 2, 3, 3})))
# (2)、使用{} -- 注意: { "name" : "张三"}是字典类型 ; { 1, 2, 3 }是集合类型
print(type({1, 2, 2, 3, 4}))
# 去重特性
print(set([1, 1, 2, 2, 3, 3]))
print(set({1, 1, 2, 2, 3, 3}))