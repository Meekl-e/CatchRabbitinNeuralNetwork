from math import cos, pi, sin
import random

f = open('bobry.svg', 'w')
f.write('<?xml version="1.0" encoding="utf-8"?>\n')
f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="10000000px" height="10000000px" >\n')
pm = -99999999
al = pi / 4
r = []
t = []
fff = 0
for i in range(40):
    a = random.randint(100, 500)
    b = random.randint(100, 500)
    
    r.append(a)
    t.append(b)
    q = f'<rect x="{a}" y="{b}" width="1" height="1" fill="red" stroke="red" stroke-width="0.1" />'
    f.write(q)
v = []
g = []
y = []
for j in range(1, 361, 1):
    pm = -999
    al = 2 * pi / 360*j
    for i in range(len(r)):
        a = r[i]
        b = t[i]
        pp = a * cos(al) + b * sin(al)
        if pp >= pm:
            pm = pp
            ba = a
            bb = b
    v.append(ba)
    g.append(bb)
xn = 1000
xm = -1000
yn = 1000
ym = -1000
iuy = 0
for i in range(len(v)):
    v2 = v[i-1]
    g2 = g[i-1]
    v1 = v[i]
    g1 = g[i]
    o = f'<line x1="{v1}" y1="{g1}" x2="{v2}" y2="{g2}" style="stroke:rgb(25,0,0);stroke-width:1" />'
    f.write(o)
    yy = (((v2 - v1)**2 + (g2-g1)**2))**0.5
    y.append(yy)
    if yy == 0.0:
        pass    
f.write(f'<line x1="300" y1="1000" x2="1020" y2="1000" style="stroke:rgb(25,0,0);stroke-width:1" />')
LX = 300
LY = 700
for i in range(len(q)):
    e = v[i]
    r = g[i]
    if e < xn:
        xn = e
        xny = r
    if e > xm:
        xm = e
        xmy = r
    if r > ym:
        ym = r
        ymx = e
    if r < yn:
        yn = r
        ynx = e
for i in range(len(y)):
    lll = y[i]
    fff = fff + lll
pfb = ((ym - yn) + (xm - xn)) * 2
pf = ((xn-ymx)**2 +(xny-ym)**2)**0.5 + ((xm-ymx)**2 +(xmy-ym)**2)**0.5 + ((xn-ynx)**2 +(xny-yn)**2)**0.5 + ((xm-ynx)**2 +(xmy-yn)**2)**0.5
itog = ((pfb - fff) / pfb) * 100
print(itog)

for i in range(len(y)):
    if y[i] < 50:
        f.write(f'<line x1="{LX}" y1="{1000}" x2="{LX}" y2="{970}" style="stroke:rgb(100,15,    87);stroke-width:1" />')
    oo = y[i]
    f.write(f'<line x1="{LX}" y1="{1000}" x2="{LX}" y2="{1000-(oo*3)}" style="stroke:rgb(25,0,0);stroke-width:1" />')
    LX = LX + 2
f.write('</svg>')
f.close()