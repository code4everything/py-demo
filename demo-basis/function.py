# coding:utf-8
import functools
import time

print()


def print_with_date(sentence):
    print(format_date(time.localtime(), "%Y-%m-%d %H:%M:%S"), sentence)


def format_date(date, date_format):
    """
    日期格式说明
    %y 两位数的年份
    %Y 四位数的年份
    %m 月份
    %d 日期
    %H 24小时制的小时数
    %I 12小时制的小时数
    %M 分钟
    %S 秒
    %w 星期

    更多格式请参考：
    https://www.runoob.com/python/python-date-time.html

    :param date: 日期
    :param date_format: 日期格式
    :return: 日期字符串
    """
    return time.strftime(date_format, date)


def do_something():
    """
    占位
    """
    pass


def return_multi_value(x, y):
    """
    其实质是返回一个元组
    """
    return x * x, y * y


def power(z, n=2):
    """
    默认参数必须是不可变对象，更多细节请查看：
    https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888
    """
    while n > 1:
        z *= z
        n -= 1
    return z


def multi_params(string, *param):
    """
    可变参数其实接收到的是一个元组
    """
    print(string, param)


def key_func(name, gender, **extra):
    """
    关键字参数接收的其实是一个字典
    """
    print('name:', name, 'gender:', gender, ',', extra)


print_with_date('how is it going?')
x, y = return_multi_value(2, 3)
print(x, y)
print(pow(2, 10))

print("test multi params:", 'param1', 'param2')
print("test multi params:", *['param1', 'param2'])

key_func('tony', 'boy', job='engineer', city='New York')


# see details:
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888


# --------------将函数作为返回值------------------------------------------

def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax += x
        return ax

    return sum


f = lazy_sum(*list(range(0, 10)))
print(f())

# -------------------------偏函数------------------------------------------

# see details:
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145929440

print()
int2 = functools.partial(int, base=2)
print(int2('1101010101'))
print(int2('2321335', base=10))
