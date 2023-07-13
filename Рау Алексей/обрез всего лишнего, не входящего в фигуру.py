from math import cos, pi, sin
import random

f = open('QWE.svg', 'w')
f.write('<?xml version="1.0" encoding="utf-8"?>\n')
f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000px" height="1000px" >\n')
#f.write('<rect x="25" y="25" width="50" height="50" fill="blue" stroke="blue" stroke-width="3" />\n')
pm = -99999999
al = pi / 4
r = []
t = []
for i in range(300):
    a = random.randint(100, 500)
    b = random.randint(100, 500)
    r.append(a)
    t.append(b)
    q = f'<rect x="{a}" y="{b}" width="1" height="1" fill="red" stroke="red" stroke-width="0.1" />'
    f.write(q)
x1 = 0
x2 = 1000
al = 0
for j in range(1, 361):
    pm = -999
    al = al+5
    for i in range(len(r)):
        a = r[i]
        b = t[i]
        pp = a * cos(al) + b * sin(al)
        if pp >= pm:
            pm = pp
    pp = pm
    print(al)
    y1 = (pp - cos(al) * x1) / sin(al)
    y2 = (pp - cos(al) * x2) / sin(al)
    t5 = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:rgb(25,0,0);stroke-width:1" />'
    #print(t5)
    f.write(t5)
f.write('</svg>')
f.close()
