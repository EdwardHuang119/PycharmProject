# -*- coding: utf-8 -*-
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,3))
# def power(x):
#     return x * x
# print(power(5))

l =  [x * x for x in range(1, 11) if x % 2  == 1]
print(l)
