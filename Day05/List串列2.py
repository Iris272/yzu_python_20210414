import random as r
scores = [100, -10, 90, 80, -80, 999]
print(scores)
# error_scores = scores.pop(1)
# print(error_scores, scores)
# error_scores = scores.pop(3)
# print(error_scores, scores)

# 利用pop()將不合理的分數挑出
error_scores = []
for x in scores:
    if x < 0 or x > 100:
        error_scores.append(x)

print(scores)
print(error_scores)
for y in error_scores:
    scores.pop(scores.index(y))

print(scores)

# 反轉
scores = [1, 7, 3, 5, 8, 2]
scores.reverse()
print(scores)

# 排序
scores.sort()
print(scores)

# 洗牌 (請先import random as r)
r.shuffle(scores)
print(scores)

