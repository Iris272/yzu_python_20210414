str = " she sell sea shell on the sea shore "
print(str)
str = str.strip()  # 除去左右空白
str = str.lstrip() # 去除左邊空白
str = str.rstrip() # 去除右邊空白
print('字串長度:', len(str))
print('有幾個s:', str.count('s'))
print('on這個字的位置:', str.find('on'))
print('off這個字的位置:', str.find('off'))
print('有無sea這個字:', '有' if str.find('sea') >= 0 else '沒有')
print('有沒有land這個字:', '有' if str.find('land') >= 0 else '沒有')
print('有幾個英文單字:', str.count(' ')+1)
# 是否都是英文字(a-z,A-Z)
# 小技巧: 先利用replace 將中間的空白去除
print('是否都是英文字:', str.replace(' ', '').isalpha())
print(str[2])  # 取第3個字元
print(str[0:3]) # 取出0-3位置的字串，但是不含3
path = 'C:\temp\nba\score.py'
print('路徑位置:', path)
pathA = r'C:\temp\nba\score.py'  # 前面加r，不解釋特殊符號
print('路徑位置:', pathA)
