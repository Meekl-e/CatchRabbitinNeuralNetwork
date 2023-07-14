import math, random
#рисует все точки, которые являются "зайцами"
def fin(x, y):
    sm = []
    k = 0
    for i in range(1, 360, 10):
        p = []
        a = 2 * math.pi / 360 * i
        for j in s:
            pntX, pntY = j
            p.append(pntX * math.cos(a) + pntY * math.sin(a))
        maxp = max(p)
        d = x * math.cos(a) + y * math.sin(a) - maxp
        if d <= 0:
            sm.append(0)
        else:
            sm.append(1)
    if sum(sm) > 0:
        return 0
    else:
        return 1

f = open('workfile', 'w')
f.write('''
<?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100px" height="100px">
''')
s = []
n = int(input())
for i in range(n):
    pntX = random.randint(10, 90)
    pntY = random.randint(10, 90)
    pnt = pntX, pntY
    s.append(pnt)
for x in range(100):
    for y in range(100):
        if fin(x, y) == 1:
            f.write(f'''
                <rect x="{x}" y="{y}" width="1" height="1" fill="black" stroke="black" stroke-width="1" />
            ''')
for i in s:
    pntX, pntY = i
    f.write(f'''
        <rect x="{pntX}" y="{pntY}" width="1" height="1" fill="red" stroke="red" stroke-width="1" />
    ''')
f.write('''
</svg>\n
''')
f.close()