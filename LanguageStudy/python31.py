from typing import Optional
from pydantic import Field

# python说明类成员的属性的方法
# 注: (Optional[str]) 等价于 (str | none)
class test:
    # 下面的self.name无法说明, 只能强制定义
    # 注: Field这种等号只适合于这种场合
    name: Optional[str] = Field(default=None, description="这个人的名字")
    def __init__(self):
        self.name = "123"