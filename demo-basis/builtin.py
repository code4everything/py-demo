# coding:utf-8

import argparse
import os
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import deque
from collections import namedtuple
from datetime import datetime

# =======================获取当前日期和时间=======================================

print(datetime.now())

dt = datetime(2019, 6, 29, 20)
print(dt)

# 转换成时间戳，这是一个浮点数，小数部分表示毫秒
t = int(dt.timestamp())
# 时间戳转日期
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

# 字符串与日期互转
print(datetime.strptime("2019-06-29 20:41:13", "%Y-%m-%d %H:%M:%S"))
print(dt.strftime("%Y-%m-%d %H:%M:%S"))

# ===================================集合===========================================

point = namedtuple("point", ['x', 'y'])
p = point(1, 2)
print(p.x, p.y)

# 双向链表，可以轻松实现栈和队列
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 有默认值的字典
d = defaultdict(lambda: 'N/A')
print(d.get('key', 'test'))
print(d['key'])

# 按插入顺序排序的字典
print(OrderedDict({'a': 1, 'b': 2, 'd': 3, 'c': 4}))

# 按定义的顺序查找
defaults = {'color': 'red', 'user': 'guest'}
# 命令行参数解析
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
chain_map = ChainMap(command_line_args, os.environ, defaults)
print(chain_map['user'])

# 计数器
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
