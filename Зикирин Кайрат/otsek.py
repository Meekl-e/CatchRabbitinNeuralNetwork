import math
import random
tochki = [] 
x1 = 0
x2 = 1000
f = open('wory21fle', 'w')
f.write('''
<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width='1000px' height="1000px">
<rect x ="0"  y = '0' width='1000' height = '1000' fill = "rgb(0, 0, 0)" stroke = 'grey' stroke-width='5'/>''')
for rfgr in range(100):
    gx = random.randint(250, 750)
    gy = random.randint(250, 750)
    tochki.append((gx, gy))
r = 10
for rfg in range(1,36):
    al = (2 * math.pi) / 360 * r#fg
    oldp = -1000000000
    for xy in tochki:
        x, y = xy
        p = x *  math.cos(al) + y * math.sin(al)
        if p >= oldp:
            oldp = p
            l = p                                               #148, 255, 255          0, 255, 55
    y2 = (l - math.cos(al) * x2) / math.sin(al)
    y1 = l / math.sin(al)
    r += 10
    f.write(f'''
        <line x1="{x1}" y1="{y1}" x2 = "{x2}" y2 = "{y2}" style='stroke:rgb(255, 255, 255); stroke-width=1'/>''')             
for p1 in tochki:
    x, y = p1
    f.write(f'''
        <circle cx="{x}" cy="{y}" r="3" stroke="white" stroke-width="0" fill="rgb(0, 255, 55)" />''')                 
f.write('</svg>\n')           
f.close    