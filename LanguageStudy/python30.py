from typing_extensions import Annotated
from typing import Union
from pydantic import Field, BaseModel

# 63、pydantic库深度理解
# 在python中，类型是动态的, 默认情况下运行是不会进行类型检查的, 但是可以通过让类继承BaseModel, 进而实现运行时检查

# 64、isinstance判断类型
a = {}
if isinstance(a, dict):
    print("a是字典类型")
else:
    print("a不是字典类型")