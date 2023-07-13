from operator import index
import random
import math
f = open("workile3","w")
f.write('''
    <?xml version = "1.0" encoding ="utf-8"?>
    <svg xmlns = "http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000px" height="1000px">
    ''')

n0 = 100
x1 = 25
y1 = 25
Answer = 0
points = []
poi = []
p = []
p2 = []
op = []






def Fi(a,b):
    if a != b:
        x1,y1=a
        x2,y2=b
        dx = x2 - x1
        dy = y2 - y1
        z = dx**2 + dy**2
        c = z**0.5
        v = dx / c
        n = math.acos(v)
        if c < 0: n = -n
        m = n * 180 / math.pi
        m = 180 - m
        p.append(m)
def Fi2(a,b):
    if a != b:
        x1,y1=a
        x2,y2=b
        dx = x2 - x1
        dy = y2 - y1
        z = dx**2 + dy**2
        c = z**0.5
        v = dx / c
        n = math.acos(v)
        m = n * 180 / math.pi 
        if dy < 0:

            p2.append(-m)
        else:
            p2.append(m)
def Cehpoint(a):
    for il in range(len(points)):
        a=(points[il], poi[il])
        Fi2(a,b)   
    l = max(p2)
    q7= p2.index(l)
    q9 = points[q7]
    q8=poi[q7]
    f.write(f'''
        <rect x={q9} y={q8} width="2" height="2" fill="red" stroke='red' stroke-width="1" />
        ''')
    op.append(l)





for i5 in range (100):
    x=random.randint(100, 1000)
    y=random.randint(100, 1000)
    a = (x,y)
    b = 0,500
    points.append(x)
    poi.append(y)
    Fi(a,b)
    f.write(f'''
        <rect x={x} y={y} width="2" height="2" fill="blue" stroke='blue' stroke-width="1" />
        ''')
l = max(p)
q7= p.index(l)
q9 = points[q7]
q8=poi[q7]
f.write(f'''
    <rect x={q9} y={q8} width="2" height="2" fill="red" stroke='red' stroke-width="1" />
    ''')
op.append(l)
b=(q9, q8)
q0 = l
answer = 0        
for i3 in range(1):
    Cehpoint()            
    b=(q9, q8)
    del p2[:]   
f.write(f'''
    <line x1="0" y1="500" x2='1000' y2='500' style='stroke:green' stroke-width="1" />
    ''')
f.write('</svg>\n')
f.close()