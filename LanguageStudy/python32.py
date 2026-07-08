from typing_extensions import Annotated
from typing import Union
from pydantic import Field

# 67、Field和Annotated的区别
# Annotated[类型, 元数据1, 元数据2, ...]: 里面元数据没有位置要求, 可以随便写, 它的用途在于给其它接口去识别, 如Field元数据给pydantic去识别
# Field()是随pydantic使用的, 简单来说, 就是给运行时检查多加几层内容而已
#                           如在pydantic下，a: str表示只检查是否为str类型; 而a: str = Field(min_length=2, max_length=50)会增加长度检查
# 下面两种写法不是等价的
age: Annotated[int, Field(..., description="年龄")]                 # 表示类型是int, 必填数, 描述为年龄
age: Annotated[int, ..., "年龄"]                                    # 元数据有... 和 年龄
name: Union[str] = Field(default=None, description="这个人的名字")   # 在继承于Basemodel的类里面才有意义