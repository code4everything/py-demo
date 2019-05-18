# coding:utf-8

print()

print('字符的整数表示：')
print('a >>', ord('a'))
print('中 >>', ord('中'))
print('66 >>', chr(98))
print('25991 >>', chr(25991))

print()

print('编解码：')
print('\'abc\' encode by ascii >>', 'abc'.encode('ascii'))
print('\'中文\' encode by utf8 >>', '中文'.encode('utf-8'))
print('b\'abc\' decode by ascii >>', b'abc'.decode('ascii'))
print('b\'\\xe4\\xb8\\xad\\xe6\\x96\\x87\' decode by utf8 >>', b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print()

print('字符长度：')
print('length of \'abc\' >>', len('abc'))
print('length of \'中文\' >>', len('中文'))
print('byte length of \'中文\' >>', len('中文'.encode('utf-8')))

print()

print('字符串的格式化：')
print('{0} {1}'.format('awesome', 'china'))
print('hello, %s' % 'python')
print('%d divide %d is %f' % (5, 2, 2.5))
# 将 % 作为普通字符格式化输出
print('%s %% %s = %s' % (3, 2, 1))
