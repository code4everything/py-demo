# coding:utf-8

import os

print("process (%s) start..." % os.getpid())

# 返回两次，仅在类Unix系统下正常工作
pid = os.fork()

if pid == 0:
    print("i am child process (%s)  and my parent is %s." % (os.getpid(), os.getppid()))
else:
    print("i (%s) just created a child process (%s)" % (os.getpid(), pid))

# 更多多进程的技术参考：
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064
