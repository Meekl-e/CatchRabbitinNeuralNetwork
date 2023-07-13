from math import cos, sin
from operator import index
import random
import math
points = []
poi = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p7 = []
alpha = [()]
def getRabbit(x, y):
    global poi, points
    answer = 0
    for ib in range(1, 361):
        oldp = - 999999999999999999999
        a1 = 2 * math.pi * ib/360
        for im in range(len(points)):
            y1 = poi[im]
            x1 = points[im]
            p = x1 * cos(a1) + y1 * sin(a1)
            p2.append(p) 
            p3.append(x1)
            p4.append(y1)
            if p >= oldp : oldp = p
        p = oldp
        q = p2.index(oldp)
        p5.append(p3[q])
        p6.append(p4[q])
        h6 = cos(a1) * x + sin(a1)*y - p
        if h6 > 0:
            answer += 1
        else:
            answer += 0
    for _1 in range(len(p5)):
        x5 = p5[_1]
        y5 = p6[_1]
        if x5!=p5[len(p5)-1]:
            x6 = p5[_1+1]
            y6 = p6[_1+1]
            av = ((x6-x5)**2+(y6-y5)**2)**0.5
            p7.append(av)
        else:
            x6 = p5[0]
            y6 = p6[0]
            av = ((x6-x5)**2+(y6-y5)**2)**0.5
            p7.append(av)

    if  answer == 0: return 1 
    else: return 0
f = open("workile5.svg","w")
f.write('''<?xml version = "1.0" encoding ="utf-8"?>
    <svg xmlns = "http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000px" height="1000px">
    ''')
for i5 in range (10):
            z = random.randint(1, 254)
            z1 = random.randint(1, 254)
            z2 = random.randint(1, 254)
            y3=random.randint(0, 20)
            x3=random.randint(0, 20)
            points.append(x3)
            poi.append(y3)
for i in range(20):
    for iz in range(20):
        if getRabbit(i, iz) == 1:
            f.write(f'''
                <circle cx="{i}" cy="{iz}" r = "0.5" fill="black" stroke="black" stroke-width="1" />
                ''')
x9 = max(points)
x10 = min(points)        
y10 = min(poi)
y9 = max(poi)
r=(x9 - x10)/2
f.write(f'''
    <rect x={x10} y={y10} width="{x9-x10}" height="{y9-y10}" fill="red" stroke='red' stroke-width="1" />
    ''')
per0 = (x9-x10)*2-(y9-y10)*2
per1 = 0
for il in range(len(p7)):
    per1 = per1 + p7[il]
aqw = (per0 - per1)/per0
zx = 2*math.pi*r
if aqw == zx:
    print("Круг")    
if aqw > zx:
    print("Треугольник")  
if aqw < zx:
    print("Квадрат")  
f.write('</svg>\n')
f.close()

           

                

    
#for i in range(len(points)):
#    f.write(f'''
#       <circle cx="{points[i]}" cy="{poi[i]}" r = "1" fill="green" stroke="green" stroke-width="1" />
#       ''')

