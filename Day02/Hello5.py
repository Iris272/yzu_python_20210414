# -*- coding:UTF-8 -*-
h = 170
w = 50
bmi = w / (h/100)**2
print("%.2f" % bmi)
print(5/2)
print(5//2)   # 無條件捨去 整除
print(5%2)    # 餘數

num = 123456789
if num % 2 == 0:
    print("偶數")
else:
    print("奇數")
