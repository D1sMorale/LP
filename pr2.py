import math
x = float(input(''Введите x: ''))
t = float(input(''Введите t: ''))
z1 = float((9*math.pi*t+10*math.cos(x)))
z2 = float((math.sqrt(t) - abs(math.sin(t)))*math.exp(x))
z3 = (z1/z2) * math.exp(x)
z3 = float('{.2f}'. format(z3))
print(z3)
