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


def reduce_test(x, y):
    print('y:', y)


# 从测试中可以看出，当列表只有一个值时，不会调用函数
print(reduce(reduce_test, [1]))
