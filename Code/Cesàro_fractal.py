import math as mt

theta = mt.radians(85)
r = 1/(2*(1 + mt.cos(theta)))
NumS = 4
a = [r, r * mt.cos(theta), r * mt.cos(theta), r]
b = [0, -r * mt.sin(theta), r * mt.sin(theta), 0]
c = [0, r * mt.sin(theta), -r * mt.sin(theta), 0]
d = [r, r * mt.cos(theta), r * mt.cos(theta), r]
e = [0, r, r + r * mt.cos(theta), r + (2 * r * mt.cos(theta))]
f = [0, 0, r * mt.sin(theta), 0]
pr = [1 / 4, 1 / 4, 1 / 4, 1 / 4]

