import math
import random
import time
tochki = [] 
x1 = 0
x2 = 1000
#dal = 0.1
#al = math.pi / 4
#y2 = (p - math.cos(al) * x2) / math.sin(al)
#y1 = p / math.sin(al)
al = 1
f = open('lines.svg', 'w')
f.write('''
<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width='1000px' height="1000px">
<rect x ="0"  y = '0' width='1000' height = '1000' fill = "rgb(0, 0, 0)" stroke = 'grey' stroke-width='5'/>''')
for rfgr in range(100):
    gx = random.randint(250, 750)
    gy = random.randint(250, 750)
    tochki.append((gx, gy))

for rfg in range(1,361, 10):
    al = (2 * math.pi) / 360 * rfg
    oldp = -1000000000
    pX = 0
    for xy in tochki:
        x, y = xy
        p = x *  math.cos(al) + y * math.sin(al)
        
        if p >= oldp:
            oldp = p
    
    y2 = (oldp - math.cos(al) * x2) / math.sin(al)
    y1 = (oldp - math.cos(al) * x1) / math.sin(al)

    f.write(f'''
        <line x1="{x1}" y1="{y1}" x2 = "{x2}" y2 = "{y2}" style='stroke:rgb(148, 255, 255); stroke-width=1'/>''')             
for p1 in tochki:
    x, y = p1
    f.write(f'''
        <circle cx="{x}" cy="{y}" r="3" stroke="white" stroke-width="0" fill="rgb(0, 255, 55)" />''')
    f.write(f'''
        <circle cx="{x}" cy="{y}" r="0.5" stroke="white" stroke-width="0" fill="orange" />''')          
   
f.write('</svg>\n')           
f.close    