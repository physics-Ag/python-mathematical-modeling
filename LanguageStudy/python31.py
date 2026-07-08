from typing import List
from pydantic import BaseModel

# 65、Python类的默认值是被共享的
class dog:
    a: int = 10
    b: List[int] = []

dog1 = dog()
dog2 = dog()
print(f"{dog1.a} + {dog1.b}")
print(f"{dog2.a} + {dog2.b}")
dog1.b.append(1)
dog1.b.append(1)
dog1.b.append(1)
dog1.a = 10
print(f"{dog1.a} + {dog1.b}")
print(f"{dog2.a} + {dog2.b}")
dog3 = dog()
print(f"{dog3.a} + {dog3.b}")
# 解决方案: 
# (1)、继承BaseModel, 想进一步的话, 可以使用Field进行定制
class dog(BaseModel):
    a: int = 10
    b: List[int] = []

dog1 = dog()
dog2 = dog()
print(f"{dog1.a} + {dog1.b}")
print(f"{dog2.a} + {dog2.b}")
dog1.b.append(1)
dog1.b.append(1)
dog1.b.append(1)
dog1.a = 10
print(f"{dog1.a} + {dog1.b}")
print(f"{dog2.a} + {dog2.b}")
dog3 = dog()
print(f"{dog3.a} + {dog3.b}")


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