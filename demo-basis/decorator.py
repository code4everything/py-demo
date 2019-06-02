# coding:utf-8

import functools


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        func(*args, **kw)
        print('call ended')

    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            func(*args, **kw)
            print('call ended')

        return wrapper

    return decorator


@log
def now():
    print('2019-06-02')


f = now
# 函数的属性已更改
print(f.__name__)
f()


@log2('装饰器测试')
def log_test():
    print('method calling')


print()
f = log_test
print(f.__name__)
f()
