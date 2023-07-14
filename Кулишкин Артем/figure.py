import math
import numpy
import random
f=open('square_circle_triangle', 'w')
f.write('''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1700px" height="1700px">\n''')
tochki = []
for i in range(30):
    a = random.randint(40, 500)
    b = random.randint(40, 500)
    tochki.append((a, b))
    f.write(f'''<circle cx="{a}" cy="{b}"  r="2" stroke="blue" stroke-width="2"/>\n''')
alfa = 0
v = []
g = []
degrees = []
alfiki = []
for i in range(1, 361):
    alfa = 2 * math.pi / 360 * i
    pmux = -999
    xox = 0
    yoy = 0
    degr = 0
    alfs = 0
    for peg in tochki:
        pmax = peg[0] * math.cos(alfa) + peg[1] * math.sin(alfa)
        if pmax >= pmux:                   
            pmux = pmax
            xox = peg[0]
            yoy = peg[1]
            degr = alfa
            alfs = alfa
    alfiki.append(alfs)
    degrees.append(degr)
    v.append(xox)
    g.append(yoy)
print('Точки\t', '          Расстояние')
dd = []
ymax = max(g)
ymin = min(g)
xmax = max(v)
xmin = min(v)
print(xmin, xmax, ymin, xmax)
f.write(f'''<line  x1="{xmin}" y1="{ymin}" x2="{xmax}" y2="{ymin}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
f.write(f'''<line  x1="{xmin}" y1="{ymin}" x2="{xmin}" y2="{ymax}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
f.write(f'''<line  x1="{xmax}" y1="{ymin}" x2="{xmax}" y2="{ymax}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
f.write(f'''<line  x1="{xmin}" y1="{ymax}" x2="{xmax}" y2="{ymax}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
perkv = ((xmax - xmin) + (ymax - ymin)) * 2
for i in range(len(v)):
    vov2 = v[i - 1]
    gog2 = g[i - 1]
    vov1 = v[i]
    gog1 = g[i]
    
    f.write(f'''<line  x1="{vov1}" y1="{gog1}" x2="{vov2}" y2="{gog2}" style="stroke:rgb(168,228,160);stroke-width:2"/>\n''')
    d = (((vov2 - vov1) ** 2) + ((gog2 - gog1) ** 2)) ** 0.5
    if d == 0:
        continue
    dd.append(d)
    print(vov2, gog2, '-', vov1, gog2, ' ', d)
print(dd)
permg = sum(dd)
print(perkv)
print(permg)
formul = ((perkv - permg) / perkv) * 100
rad = perkv / 8
krug = (4 - math.pi) / 4 * 100
print(krug)
if len(dd) == 4:
    if dd[1] / dd[3] >= 3 or dd[0] / dd[2] >= 3:
        print('Это четырехугольник')
    else:
        print('Это квадрат')
elif len(dd) == 3 or formul >= 25:
    print('Это треугольник')
elif formul <= 25:
    print('Это квадрат')
elif formul <= krug and len(dd) > 13:
    print('Это круг')

print(formul)
"""for i in range(len(dd)):
    if dd[i] == 0:
        f.write(f'''<line  x1="{lx}" y1="{375}" x2="{lx}" y2="{400}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
    buk = dd[i]
    f.write(f'''<line  x1="{lx}" y1="{400 - buk}" x2="{lx}" y2="{400}" style="stroke:rgb(255,151,187);stroke-width:2"/>\n''')
    lx += 4"""
f.write('\n</svg>')
f.close

