# coding:utf-8

import re

# 返回一个 Match 对象
match = re.match(r'\d{3}\-\d{3,8}', '010-12345')

if match:
    print("匹配成功")
    print(match.group(0))
else:
    print("匹配失败")

# 编译正则表达式
regexp = re.compile(r'^\d+?$')
print(regexp.match('233'))
