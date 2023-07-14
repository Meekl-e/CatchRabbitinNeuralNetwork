import math, random
#определяет, в какой области могут быть "зайцы"
f = open('workfile', 'w')
f.write('''
<?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000px" height="1000px">
''')
s = []
n = int(input())
x0, x1 = 0, 1000
for i in range(n):
    pntX = random.randint(100, 900)
    pntY = random.randint(100, 900)
    pnt = pntX, pntY
    s.append(pnt)
for a in range(1, 360):
    p = []
    for i in s:
        pntX, pntY = i
        p.append(pntX * math.cos(a) + pntY * math.sin(a))
    maxp = max(p)
    y0 = (maxp - math.cos(a) * x0) / math.sin(a)
    y1 = (maxp - math.cos(a) * x1) / math.sin(a)
    f.write(f'''
        <line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" style="stroke:rgb(255,255,255);stroke-width:0.5;stroke:rgb(0,0,0)"/>
    ''')
for i in s:
    pntX, pntY = i
    f.write(f'''
        <rect x="{pntX}" y="{pntY}" width="2" height="2" fill="red" stroke="red" stroke-width="1" />
    ''')
f.write('''
</svg>\n
''')
f.close()