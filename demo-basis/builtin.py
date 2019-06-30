# coding:utf-8

import argparse
import base64
import hashlib
import hmac
import itertools
import os
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import deque
from collections import namedtuple
from contextlib import closing
from contextlib import contextmanager
from datetime import datetime
from urllib.request import urlopen

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

# ==================================================BASE64编码=================================================

b = base64.encodebytes(b'yoo, cool')
print(b)
print(base64.decodebytes(b))
print(base64.urlsafe_b64encode(b'/user?name=guest'))

# ===================================================加密==================================================

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
sha2 = hashlib.sha256()
sha2.update('test sha256'.encode('utf-8'))
print(sha2.hexdigest())
print(hmac.new(b'salt', b'hello dear', digestmod='md5').hexdigest())

# =======================================================迭代工具================================================

# 如果没有重复次数，将无限重复下去
bs = itertools.repeat('a', 8)
for b in bs:
    print(b)
# 把一组迭代对象串联起来
bs = itertools.chain('abc', 'def')
for b in bs:
    print(b)
# 把迭代器中相邻的重复元素挑出来放在一起
for k, g in itertools.groupby('aaabbbccaa'):
    print(k, list(g))


# 更多应用，请参考：
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017783145987360

# ===========================================================上下文管理================================================

class Query(object):

    def __init__(self, name: str):
        self.name = name

    def query(self):
        print('query about %s' % self.name)


@contextmanager
def create_query(name: str) -> Query:
    print('begin')
    q = Query(name)
    yield q
    print('end')


# 实现了上下文管理的对象，可以使用with语句来实现自动关闭资源
with create_query('bob') as q:
    q.query()
# 没有实现上下文管理的，可以用closing来实现
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
