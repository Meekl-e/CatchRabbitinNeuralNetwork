import math
import random

tochki = [] 
tochkip = []
f = open('allPoints.svg', 'w')
f.write('''<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<svg width="200`" height="200" xmlns="http://www.w3.org/2000/svg">''')
def toc(x1, y1):
    pcords = []
    ot = 0
    for rfg in range(1,361):
        al = (2 * math.pi) / 360 * rfg
        oldp = -1000000000
        pcord = 0
        for xy in tochki:
            x, y = xy
            p = x *  math.cos(al) + y * math.sin(al)
            if p >= oldp:
                oldp = p
                pcord = x, y 
        p = oldp
        pcords.append(pcord)
        d = x1 *  math.cos(al) + y1 * math.sin(al) - p
        if d > 0: return 0 

    
    return 1
f.write('''
        <line x1="200" y1="200" x2 = "200" y2 = "400" style='stroke:rgb(255, 0, 0); stroke-width=1'/>''')      

for rfgr in range(20):
    gx = random.randint(10, 180)
    gy = random.randint(10, 180)
    tochki.append((gx, gy))
    
for x in range(0,200, 4):
    for y in range(0,200, 4):
        g = toc(x, y)
        
        if g == 1:
            f.write(f'''
        <circle cx="{x}" cy="{y}" r="2" stroke="white" stroke-width="0" fill="black" />''')

for x,y in tochki:
    f.write(f'<circle cx="{x}" cy="{y}" r="5" stroke="yellow" stroke-width="0" fill="yellow" />')

f.write('</svg>\n')           
f.close()