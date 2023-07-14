from matplotlib import pyplot as plt
from numpy import arctan, copysign, pi, cos, sin
from numpy.random import random
from vector import Vector2, Point


def azimuth(center=Vector2(0, 0), poi=Vector2(0, 0)):
    return (90 - arctan((poi.y - center.y) / (poi.x - center.x)) * 180 / pi + -90 * (copysign(-1, (poi.x - center.x)) + 1)) % 360


def findGap(seq):
    seq += [seq[0]]
    res = []
    for i in range(len(seq) - 1):
        res.append((seq[i + 1] - seq[i]) % 360)
    return max(res)


n = 1000
pSet = {Vector2(*random(2) * 2 - 1) for i in range(int(n * 4 / pi))}
pSet = set(filter(lambda x: abs(x + Vector2(0, 0)) < 2, pSet))
hull = []
center = Vector2(0, 0)
for i in pSet:
    center += i
center /= len(pSet)

for i in pSet:
    azis = []
    for j in pSet - {i}:
        azis.append(azimuth(i, j))
    if findGap(sorted(azis)) > 180:
        hull.append(i)
hull.sort(key=lambda x: azimuth(center, x))

angles = []
for i1, i2, i3 in zip(hull, hull[1:] + [hull[0]], hull[2:] + [hull[0], hull[1]]):
    angles.append((azimuth(i2, i3) - azimuth(i1, i2)) % 360)
order = [i for i in range(len(angles))]
order.sort(key=lambda x: angles[x])

hull.append(hull[0])
plt.scatter([i.x for i in pSet - set(hull)], [i.y for i in pSet - set(hull)])
plt.scatter([i.x for i in hull], [i.y for i in hull], color='red')
plt.plot([i.x for i in hull], [i.y for i in hull], color='red')
plt.show()

plt.bar([i for i in range(len(angles))], angles)
plt.show()

print(order)