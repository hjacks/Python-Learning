# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:03:57 2017

@author: Administrator
"""

import sys

sys.path.append('C:/Users/Administrator/Desktop')
import hello

hello.hello()

# 在主程序中，__name__的值是__main__，在导入的模块中是模块名
print(__name__)
print(hello.__name__)


def hello4():
    print('hhhh')


def test():
    print('This is test demo')


if __name__ == '__main__': test()

# 查看模块的存放地址
import pprint

pprint.pprint(sys.path)

# 2.1 模块中有什么
# 1 使用dir
import copy

print(dir(copy))
print([n for n in dir(copy) if not n.startswith('_')])

# 2 all变量
print(copy.__all__)
# 使用 from copy import * 代码，就只能使用all中的3个函数，使用其他的就得显示引入

# 2.2 使用help
help(copy.copy)

# 2.3 文档
print(range.__doc__)

# 2.4 阅读源代码
print(copy.__file__)  # 得到copy模块源代码地址

# 3 标准库
# 3.1 sys
# sys中一些重要函数和变量
# argv           命令行参数，包括脚本名称
# exit([arg])    退出当前程序，可选参数为给定的返回值或错误信息
# modules        映射模块名字到载入模块的字典
# path           查找模块所在目录的目录名列表
# platform       类似sunos5或win32的平台标识符
# stdin          标准输入流----一个类文件对象
# stdout         标准输出流----一个类文件对象
# stderr         标准错误流----一个类文件对象

# 反序打印命令行参数
import sys

arg = sys.argv[1:]
arg.reverse()
print(' '.join(arg))

# 3.2 os
# os中一些重要函数和变量
# environ         对于环境变量进行映射
# system(command) 在子shell中执行操作系统命令
# sep             路径中的分隔符
# pathsep         分隔路径的分隔符
# linesep         行分隔符（\n,\r,\r\n）
# urandom(n)      返回n字节的加密强随机数据


# 3.3 fileinput
# input([files[,inplace[,backup]]])   #便于遍历多个输入流的行
# filename          返回当前文件的名称
# lineno            返回当前（累计）的行数
# isfristline       查询当前行是否是文件的第一行
# isstdin           检测最后一行是否来自sys.stdin
# nextfile          关闭当前文件，移动到下一个文件
# close             关闭序列

# 3.4集合，堆和双端序列
# 1.集合(set)
print(set(range(10)))
# 检查成员资格，因此忽略重复值
print(set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
# 和字典一样，顺序随意
print(set(['foo', 'nad', 'dde']))
a = set([1, 2, 3])
b = set([2, 3, 4])
print(a.union(b))
print(a | b)
c = a & b
print(c.issubset(a))
print(c <= a)
print(c.issuperset(a))
print(c > a)
print(a.intersection(b))
print(a & b)
print(a.difference(b))
print(a.symmetric_difference(b))
print(a ^ b)
print(a.copy())
print(a.copy() is a)
# 集合可变，不能做字典的键，集合本身只能包含不可变的值，故集合不能包含集合，但实际上集合的集合
# 很常见，所以可以用frozenset类型，用于代表不可变集合
a = set()
b = set()
# a.add(b)
# >TypeError: unhashable type: 'set'
a.add(frozenset(b))
print(a)

# 2.堆（heap)
# python没有独立的堆模型，只有一个包含一些堆操作函数的模块--heapq
# heapq模块常用函数
# heappush(heap,x)          将x入堆
# heappop(heap)             将堆中最小元素弹出
# heapify(heap)             将heap属性强制应用到任意一个列表
# heapreplace(heap,x)       将堆中最小元素弹出，同时将x入堆
# nlargest(n,iter)          返回iter中第n大元素
# nsamllest(n,iter)         返回iter中第n小元素

from heapq import  *
from random import  shuffle
data=list(range(10))
shuffle(data)
print(data)
heap=[]
for n in data:
    heappush(heap,n)
print(heap)
heappush(heap,0.5)
print(heap)
x=heappop(heap)
print(x)
y=heappop(heap)
print(y)
print(heap)
#heapify用任何列表作为参数，并转换为合理的堆
heap=[8,6,3,7,1,4,2,9,5,0]
heapify(heap)
print(heap)
heapreplace(heap,0.2)
print(heap)

#3.双端队列
from collections import  deque
q=deque(range(5))
print(q)
q.append(5)
q.appendleft(6)
print(q)
x=q.pop()
y=q.popleft()
print(x,y)
print(q)
#rotate，左移或右移
q.rotate()
print(q)
q.rotate(2)
print(q)
q.rotate(-1)
print(q)

#3.5.time
#日期可以用实数或者是包含有9个整数的元组表示
#python日期元组各字段意义
#索引      字段       值
#0         年        2017,2016等
#1         月        1-12
#2         日        1-31
#3         时        0-23
#4         分        0-59
#5         秒        0-61
#6         周        0-6
#7         儒令日     1-366
#8         夏令时     0，-1,1
