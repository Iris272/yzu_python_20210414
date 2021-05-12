# List串列與Tuple元祖
a = [1, 2, 3, 4, 5] #  可修改
b = (1, 2, 3, 4, 5) #  不可修改
print(type(a), a)
print(type(b), b)
# 轉換
# List轉Tuple
a = tuple(a)
print(type(a), a)
# Tuple轉List
b = list(b)
print(type(b), b)

