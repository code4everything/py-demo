# encoding:utf-8

from functools import reduce


def power(x):
    return x * x


# map 函数接受两个参数，一个是函数，一个是可迭代的对象
print(list(map(power, list(range(0, 10)))))


def concat(x, y):
    return x * 10 + y


# reduce 同样接受两个参数，一个函数（该函数接受两个参数），一个可迭代的对象
print(reduce(concat, list(range(1, 10))))

# 从测试中可以看出，当列表只有一个值时，不会调用函数
print(reduce(lambda x, y: print('y:', y), [1]))


def odd(x):
    return x & 1 == 1


# 过滤
print(list(filter(odd, list(range(0, 10)))))

li = [9, 8, -7, 2, 6, -1]

# 排序
print(sorted(li, key=abs, reverse=True))
