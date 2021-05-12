# 印出 2~100 間的質數
x = int
for x in range(2, 101, 1):
    for y in range(1, x+1, 1):
        if x % y == 0 and y == 1 and y == x:
            print(x)
