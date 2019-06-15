# coding:utf-8
from enum import Enum, unique


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def users(self, username):
        return self.__getattr__(username)

    def __call__(self, *args, **kwargs):
        return "instance directly call"

    __repr__ = __str__


print(Chain().api.user.timeline.list)

print(Chain().api.users("easepan").timeline.list)

print(Chain()())

# 枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# unique is to insure here is no duplicate items
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Fri, Weekday.Fri.value, Weekday(5))

# important knowledge, but a little hard
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072
