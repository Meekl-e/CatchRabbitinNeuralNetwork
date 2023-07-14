from math import cos, sin
from operator import index
import random
import math
aa2 = []
bb3 = []
cc4 = []
dd5 = []
ee6 = []
ff7 = []
points = []
opoints = []
alpha = [()]
def getRabbit(x, y):
    global opoints, points
    answer = 0
    for ib in range(1, 361):
        oldp = - 999999999999999999999
        a1 = 2 * math.pi * ib/360
        for im in range(len(points)):
            y1 = opoints[im]
            x1 = points[im]
            p = x1 * cos(a1) + y1 * sin(a1)
            aa2.append(p) 
            bb3.append(x1)
            cc4.append(y1)
            if p >= oldp : oldp = p
        p = oldp
        q = aa2.index(oldp)
        dd5.append(bb3[q])
        ee6.append(cc4[q])
        h6 = cos(a1) * x + sin(a1)*y - p
        if h6 > 0:
            answer += 1
        else:
            answer += 0
    for _1 in range(len(dd5)):
        x5 = dd5[_1]
        y5 = ee6[_1]
        if x5!=dd5[len(dd5)-1]:
            x6 = dd5[_1+1]
            y6 = ee6[_1+1]
            av = ((x6-x5)**2+(y6-y5)**2)**0.5
            ff7.append(av)
        else:
            x6 = dd5[0]
            y6 = ee6[0]
            av = ((x6-x5)**2+(y6-y5)**2)**0.5
            ff7.append(av)

    if  answer == 0: return 1 
    else: return 0
f = open("Yar127.svg","w")
f.write('''<?xml version = "1.0" encoding ="utf-8"?>
    <svg xmlns = "http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="10000px" height="10000px">
    ''')
for tt in range (10):
            z = random.randint(1, 254)
            z1 = random.randint(1, 254)
            z2 = random.randint(1, 254)
            y3=random.randint(0, 20)
            x3=random.randint(0, 20)
            points.append(x3)
            opoints.append(y3)
for i in range(20):
    for iz in range(20):
        if getRabbit(i, iz) == 1:
            f.write(f'''
                <circle cx="{i}" cy="{iz}" r = "0.5" fill="black" stroke="black" stroke-width="1" />
                ''')
x9 = max(points)
x10 = min(points)        
y10 = min(opoints)
y9 = max(opoints)
r=(x9 - x10)/2
f.write(f'''
    <rect x={x10} y={y10} width="{x9-x10}" height="{y9-y10}" fill="red" stroke='red' stroke-width="1" />
    ''')
per0 = (x9-x10)*2-(y9-y10)*2
per1 = 0
for il in range(len(ff7)):
    per1 = per1 + ff7[il]
aqw = (per0 - per1)/per0
zx = 2*math.pi*r
if aqw > zx:
    print("Тр")  
if aqw < zx:
    print("Кв") 
if aqw == zx:
    print("Кр")
f.write('</svg>\n')
f.close()
