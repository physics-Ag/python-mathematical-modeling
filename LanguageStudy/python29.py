from typing import Iterator
import asyncio

# 60、yield关键字
# 1、yield搭配循环 -- 在循环里面的yield不会退出, 而是把每次返回的内容保存在一个可迭代对象里面
# split_into_string的作用是把字符串按句号进行 分割 并返回一个 分割好的字符串迭代对象
def split_into_string(input: Iterator[str]) -> Iterator[str]:
    tmp = ""
    for i in input:
        tmp += i
        while "。" in tmp:
            stop_index = tmp.index("。")
            yield tmp[:stop_index]
            tmp = tmp[stop_index + 1:]
    yield tmp
# 2、yield不搭配循环单独使用, 会直接返回一个函数对象, 这个函数对象记录当前执行到的位置, 通过next函数跳转
def func():
    yield "第一次返回"
    print("准备ing")
    yield "第二次返回"
    print("准备ing")
    yield "第三次返回"
a = split_into_string("1。我的娃。无法测温。范围。123123")
for i in a:
    print(i)
# 不同函数对象
print(next(func()))
print(next(func()))
print(next(func()))
# 同一函数对象
a = func()
print(next(a))
print(next(a))
print(next(a))

# 61、python协程
# 协程的本质：在一个事件循环中，如果出现了等待任务，可以在等待过程中执行其它任务(单进程/线程)
# 协程的原理：1、协程需要一个事件循环even loop, 该事件循环会在 任务 交出执行权时选择当前的最佳任务
#            2、对于async def/with/for xxxx的部分, 调用时会直接返回一个coroutine对象, 注意!它不是一个任务
#            3、asyncio.run(xxx())会创建事件循环, 并将xxx()返回的coroutine对象转化为一个任务
#            4、await coroutine对象, 首先会把coroutine对象变成任务, 其次会声明当前任务必须在该任务执行完后才能执行，最后会把执行权交给事件循环
#            5、task1 = asyncio.create_task(func1())可以把func1()返回的coroutine对象变成任务
async def func1():
    # 创建任务, 同时交出执行权
    await asyncio.sleep(2)
    print("func1()")

async def func2():
    # 创建任务, 同时交出执行权
    await asyncio.sleep(5)
    print("func2()")

async def main():
    # 创建任务
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())

    # 创建任务, 同时交出执行权
    await asyncio.sleep(3)
    print("main()")

    # 只是声明任务依赖关系
    await task1
    await task2

# 创建事件循环 + 任务main
asyncio.run(main())

# 62、tying与typing_extensions包
# 本质就是对Python类型进行扩展的包
# 在typing中：
# Iterator[str]表示这是一个可迭代对象, 迭代的内容是str
# Iterator[List[str]]表示这是一个可迭代对象, 迭代的内容是List[str]
# Callable[[int], str]表示这是一个接受int类型的参数并返回一个str类型的函数
# Union[int, float] = None表示这是一个默认为None, 要么为str要么为float的值
# Optional[int] = None是Union[int] = None的特殊写法, !!注意Optional[int]里面只能放一个类型!!
# Literal[1, "123"]表示这是一个要么为1要么为"123"的值, 注意这个Literal[1, "123"]整体也算一个类型, 可以放在Union里面去
# any表示这是一个任意类型的值
# TypeDict是用于给字典类型添加类型注释的, 只需让类继承TypeDict即可(见下面的例1)
# 在typing_extensions中
# age: Annotated[int, ..., "年龄"]表示age是int类型, 必须有值, 这个参数是表示年龄

# 例1:
from typing import TypedDict
class User(TypedDict):
    name: str
    age: int
    email: str
user: User = { "name": "张三", "age": 25, "email": "zhangsan@example.com" }

# 在python中, 类型是动态的, 所以需要类型检查器去检查类型, 而typing库、typing_extensions库、基本类型库都是用于给类型检查器去检查类型用的!而非运行python代码用的
# 类型检查器介绍:
# mypy是用python编写的一个类型检查器, 可以使用pip install mypy安装
# 可以使用(mypy python代码)检查一段python代码的类型是否符合要求