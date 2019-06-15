# coding:utf-8

import logging


def division(n1, n2):
    return n1 / n2


def division2(n1, n2):
    if n2 == 0:
        # 主动抛出异常
        raise ValueError("value error")
    return division(n1, n2)


try:
    division2(2, 0)
except ZeroDivisionError as e:
    print("division must not be zero")
except Exception as e:
    logging.exception(e)
else:
    print("no error")
finally:
    print("try end")

print("program end")
