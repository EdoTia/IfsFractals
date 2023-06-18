import math as mt

theta = 45
NumS = 3
a = [pow(mt.cos(theta), 2), pow(mt.sin(theta), 2), 1]
b = [-mt.cos(theta) * mt.sin(theta), mt.cos(theta) * mt.sin(theta), 0]
c = [mt.cos(theta) * mt.sin(theta), -mt.cos(theta) * mt.sin(theta), 0]
d = [pow(mt.cos(theta), 2), pow(mt.sin(theta), 2), 1]
e = [0, pow(mt.cos(theta), 2), 0]
f = [1, 1 + mt.cos(theta) * mt.sin(theta), 0]
pr = [1 / 3, 1 / 3, 1 / 3]
