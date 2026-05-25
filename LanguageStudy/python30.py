from typing import TypedDict, Optional
from typing_extensions import Annotated
from pydantic import Field, BaseModel

# 63、python的Field、TypeDict、BaseModel、Annotated深度理解
# (1)、在python中，类型是动态的, 默认情况下运行是不会进行类型检查的, BaseModel就是用于做运行时类型检查的类, 只需让类继承BaseModel就可以进行运行检查, 同时还会为继承的类创建其对应的构造函数
# (2)、在python中，类型是动态的, 默认情况下语法服务器时不会进行类型检查的，TypeDict就是用于语法服务器针对于字典类型做类型检查的, 只需让类继承TypeDict就可以让语法服务器对字典类型进行检查
# (3)、Field和Annotated都是用于类型说明的, 只不过Field是元数据对象, 里面放着许多(key, value)键值对, 而Annotated是一个存放类型与元数据的容器, 两者可以搭配使用
# 下面两种写法是等价的
age: Annotated[int, Field(..., description="年龄")]
age: Annotated[int, ..., "年龄"]

# 64、isinstance判断类型
a = {}
if isinstance(a, dict):
    print("a是字典类型")
else:
    print("a不是字典类型")