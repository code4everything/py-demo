# coding:utf-8

from collections.abc import Iterable
import os

print('\n切片\n')

# ---------------------切片---------------------------

li = [1, 2, 3, 4, 5, 6]

print(li[0:3])
# 当索引从零开始时可省略
print(li[:3])
print(li[-3:])
# 每两个取一个
print(li[-6:-2:2])

# --------------------迭代------------------------------

print('\n迭代\n')

if isinstance(li, Iterable):
    result = ''
    for i in li:
        result += str(i)
    print(result)
    print()
    for i, v in enumerate(li):
        print(i, v)

print()
kv = {'a': 1, 'b': 2}

if isinstance(kv, Iterable):
    ks = ''
    for k in kv:
        ks += k
    print(ks)

    vs = ''
    for v in kv.values():
        vs += str(v)
    print(vs)

    kvs = ''
    for k, v in kv.items():
        kvs += '%s:%d, ' % (k, v)
    print(kvs)

print()

for c in 'abc':
    print(c)

# ----------------------列表生成器-----------------

print('\n列表生成器\n')

print(list(range(0, 10)))
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'abc' for n in 'xyz'])
print([d for d in os.listdir('.')])
print([k + '=' + str(v) for k, v in kv.items()])
