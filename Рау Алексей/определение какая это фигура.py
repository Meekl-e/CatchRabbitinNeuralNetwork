from math import pi, cos, sin
import random

f = open('enot.svg', 'w')
f.write('<?xml version="1.0" encoding="utf-8"?>\n')
f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="10000000px" height="10000000px" >\n')
xn = 1000
xm = -1000
yn = 1000
ym = -1000
q = []
yyy = []
w = []
z = []
c = []
for i in range(30):
    aaa = random.randrange(100, 500)
    bbb = random.randrange(100, 500)
    qq = f'<rect x="{aaa}" y="{bbb}" width="1" height="1" fill="red" stroke="red" stroke-width="0.1" />'
    f.write(qq)
    q.append(aaa)
    w.append(bbb)
for j in range(1, 361, 1):
    pm = -999
    al = 2 * pi / 360*j
    for i in range(len(q)):
        a = q[i]
        b = w[i]
        pp = a * cos(al) + b * sin(al)
        if pp >= pm:
            pm = pp
            ba = a
            bb = b
    z.append(ba)
    c.append(bb)

for i in range(len(q)):
    e = q[i]
    r = w[i]
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
for i in range(len(z)):
    v2 = z[i-1]
    g2 = c[i-1]
    v1 = z[i]
    g1 = c[i]
    o = f'<line x1="{v1}" y1="{g1}" x2="{v2}" y2="{g2}" style="stroke:rgb(25,0,0);stroke-width:1" />'
    f.write(o)
    yy = (((v2 - v1)**2 + (g2-g1)**2))**0.5
    
    if yy == 0.0:
        continue
    else:
        yyy.append(yy)
f.write(f'<line x1="{xn}" y1="{ym}" x2="{xn}" y2="{yn}" style="stroke:rgb(25,0,0);stroke-width:1" />')
f.write(f'<line x1="{xn}" y1="{ym}" x2="{xm}" y2="{ym}" style="stroke:rgb(25,0,0);stroke-width:1" />')
f.write(f'<line x1="{xm}" y1="{yn}" x2="{xm}" y2="{ym}" style="stroke:rgb(25,0,0);stroke-width:1" />')
f.write(f'<line x1="{xm}" y1="{yn}" x2="{xn}" y2="{yn}" style="stroke:rgb(25,0,0);stroke-width:1" />')
pfb = ((ym - yn) + (xm - xn)) * 2
pf = 0
for i in range(len(yyy)):
    u = yyy[i]
    pf = pf + u
itog = ((pfb - pf) / pfb) * 100
ii = []
for i in range(len(yyy)):
    if yyy[i] > 30:
        ii.append(yyy[i])
if len(ii) == 3:
    print('это треугольник')
elif len(ii) == 4:
    print('это квадрат')
else:
    print('это', len(yyy), 'угольник')
print(itog)
f.write('</svg>')
f.close()