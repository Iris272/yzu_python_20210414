import math
def getBMI(h, w):
    bmi = w / math.pow(h / 100, 2)
    return bmi
def getResult(bmi):
    result = "過輕"
    if 18 < bmi <= 23:
        result = "正常"
    elif bmi > 23:
        result = "過重"
    return result
def getBMIandResult(h, w):
    bmi = getBMI(h, w)
    result = getResult(bmi)
    return bmi, result
bmi1, result1 = getBMIandResult(180, 70)
print(bmi1, result1)

def f(n):
    if n == 0 or n == 1:
        return n
    return f(n-1) + f(n-2)
n = 30
value = f(n)
print(n,value)

a = 123 * 456 * 7.89
print("%.2f" % a)
print(format(float("%.2f" % a),","))
print("{:,}".format(a))
print("{:,}".format(float("%.2f" % a)))
