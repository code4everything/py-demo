#!/usr/bin/env python3
# coding:utf-8

"""hello python module"""

__author__ = 'Ease Pan'

# 私有变量
_private = 'private'


# 私有方法
def _hello():
    print('hello python module', _private)


def public():
    print('public method')


if __name__ == '__main__':
    _hello()
