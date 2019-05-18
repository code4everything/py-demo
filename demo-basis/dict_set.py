# coding:utf-8

# ----------------------------字典------------------------------

# 字典是无序的，对内存的消耗较大，查找数据极快，与列表正好相反，并且字典的键必须是不可变对象，避免哈希混乱的情况

print()

month = {'January': 31, 'February': 29, 'March': 31, 'April': 30}

if 'February' in month:
    print(month['February'])

month['February'] = 28

# 使用 get 方法避免抛出异常
print(month.get('May', 31))
# 删除
month.pop('January')

print()

# -----------------------------集合-------------------------------------

# 集合同字典一样是无序的，并且不重复，只有键，没有值

day = {'morning', 'noon', 'afternoon', 'evening'}

# 删除
day.remove('noon')
print(day)
# 添加
day.add('noon')

s = {'noon', 'night'}

# 交集
print(s & day)
# 并集
print(s | day)
