import math, random
#определяет какая фигура: треугольник, квадрат или круг
f = open('workfile', 'w')
f.write('''
<?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000px" height="1000px">
''')
f.write('''
    <rect x="1" y="1" width="1000" height="1000" fill="black" stroke="black" stroke-width="1" />
''')
s = []
X = []
Y = []
n = int(input())
x0, x1 = 0, 1000
for i in range(n):
    pntX = random.randint(100, 900)
    pntY = random.randint(100, 900)
    pnt = pntX, pntY
    X.append(pntX)
    Y.append(pntY)
    s.append(pnt)
ygl = set()
a_ygl = []
for a in range(1, 360):
    p = []
    for i in s:
        pntX, pntY = i
        p.append(pntX * math.cos(a) + pntY * math.sin(a))
    maxp = max(p)
    for i in range(len(s)):
        pntX, pntY = s[i]
        if pntX * math.cos(a) + pntY * math.sin(a) == maxp:
            ygl.add(s[i])
            break
    y0 = (maxp - math.cos(a) * x0) / math.sin(a)
    y1 = (maxp - math.cos(a) * x1) / math.sin(a)
    #f.write(f'''
    #    <line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" style="stroke:rgb(255,0,0);stroke-width:0.5;stroke:rgb(255,0,0)"/>
    #''')
ygl_l = []
ln = []
for i in ygl:
    pntX, pntY = i
    ygl_l.append(i)
for i in range(len(ygl_l) - 1):
    x0, y0 = ygl_l[i]
    x1, y1 = ygl_l[i + 1]
    a, b = x0 - x1, y0 - y1
    ln.append(math.sqrt(a ** 2 + b ** 2))
x0, y0 = ygl_l[-1]
x1, y1 = ygl_l[0]
a, b = x0 - x1, y0 - y1
ln.append(math.sqrt(a ** 2 + b ** 2))
per_ln = sum(ln)
print(len(ygl))
print(ln)
print(per_ln)
per = 2 * (abs(max(X) - min(X)) + abs(max(Y) - min(Y)))
wolf = 0
beer = 0
hArE = 0
res = (per - per_ln) / per * 100
if res > 15 or len(ygl) == 3:
    print('Треугольник')
elif res < 2:
    print('Квадрат')
else:
    print('Круг')
for i in ygl_l:
    pntX, pntY = i
    f.write(f'''
        <rect x="{pntX - 5}" y="{pntY - 5}" width="10" height="10" fill="white" stroke="white" stroke-width="1" />
    ''')
f.write('''
</svg>\n
''')
f.close()