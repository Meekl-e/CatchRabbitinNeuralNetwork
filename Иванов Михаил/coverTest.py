from math import pi

from matplotlib import pyplot as plt
from numpy import linspace

from vector import Point
from numpy.random import random


n = 100
coverageCircle = [0 for _ in range(142)]
coverageSquare = [0 for _ in range(142)]
coverageTriang = [0 for _ in range(142)]
r = 0.8
tNum = 0.5773502691896
tSize = r * (tNum + 1)
a = (r * pi ** 0.5) / 2
for i in range(n):
    p = Point(random(2) * 2 - 1)
    dist = abs(p.pos)
    if dist < r:
        coverageCircle[int(dist * 100)] += 1
    if -a < p.pos.x < a  and  -a < p.pos.y < a:
        coverageSquare[int(dist * 100)] += 1
    if tNum * p.pos.x + tNum * tSize > p.pos.y > -tNum * p.pos.x - tNum * tSize and  p.pos.x < 0.5 * tSize:
        coverageTriang[int(dist * 100)] += 1


plt.plot(linspace(0, 2 * r, 120), [sum(coverageCircle[:i]) / sum(coverageCircle) for i in range(120)], color='red')
plt.plot(linspace(0, 2 * r, 120), [sum(coverageSquare[:i]) / sum(coverageSquare) for i in range(120)], color='green')
plt.plot(linspace(0, 2 * r, 120), [sum(coverageTriang[:i]) / sum(coverageTriang) for i in range(120)], color='blue')
plt.plot([1.077, 1.077], [0, 1], color='black')
plt.show()

print('Круг:       ', sum(coverageCircle[:80]) / sum(coverageCircle))
print('Квадрат:    ', sum(coverageSquare[:80]) / sum(coverageSquare))
print('Треугольник:', sum(coverageTriang[:80]) / sum(coverageTriang))