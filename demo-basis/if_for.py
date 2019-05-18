# coding:utf-8

import list_tuple

print()

# -----------------------条件判断-----------------------

age = int(input('please input you age: '))

print()

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

print()

# ----------------------循环-------------------------------

for day in list_tuple.week:
    print(day)

cntSum = 0
for i in range(1, 100):
    cntSum += i

print()
print(cntSum)

while cntSum > 0:
    # why are there no ++ and -- operators, see:
    # https://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python
    cntSum -= 1

    if cntSum % 2 == 0:
        cntSum /= 2
        continue

    if cntSum % 999 == 0:
        break

print()
print('end while')
