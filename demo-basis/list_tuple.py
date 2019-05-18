# coding:utf-8

print()

# -------------------------------列表----------------------

languages = ['c', 'java', 'php', 'go']

print('length of list >>', len(languages))

# 正序
print(languages[0], languages[1])
# 倒序
print(languages[-1], languages[-2])
# 追加
languages.append("python")
# 插入指定位置
languages.insert(1, 'c#')
# 删除最后一个
languages.pop()
print('delete the last item >>', languages)
# 删除指定索引的元素
languages.pop(0)
print('delete the first item >>', languages)
languages.pop(0)
# 修改元素
languages[1] = 'python'
print(languages)

print()

# ------------------------------------元组---------------------------------

# 元组可以理解为不可变的列表，更安全，能用元组时尽可能的使用元组

# 当元组只有一个元素时，需要加一个逗号，以免误解成数学计算意义上的括号
t = (1,)
print(t)
print(t[0])

week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(week)
