from asyncio import sleep
import random
import math
import time
f=open('Yar127', 'w')
f.write('''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20000px" height="20000px">''')
f.write(f'''<rect x="0" y="0" width="10000000" height="10000000" stroke="black" fill="black" stroke-width="5"/>''')
tochechki=[]
tochechki2=[]
xa = 3900
xb=0
a1 = 0
for i in range(999):
    x1 = random.randint(100, 600)
    y1 = random.randint(100, 600)
    tochechki.append(x1)
    tochechki2.append(y1)
    f.write(f'''<circle cx="{x1}" cy="{y1}" r="4" fill="white" stroke="blue" stroke-width="1" />''')
for  im in range(1, 361):
    oldp=-999
    a1=2 * math.pi/360*im
    for i in range(len(tochechki)):
        y3=tochechki2[i]
        x3=tochechki[i]
        p= x3*math.cos(a1)+y3*math.sin(a1)
        if p >= oldp:
            oldp =p
    p=oldp
    y3=(p-math.cos(a1)*xa)/math.sin(a1) 
    y2=(p-math.cos(a1)*xb)/math.sin(a1)    
    f.write(f'''<line x1="{xa}" y1="{y3}" x2="{xb}" y2="{y2}" style='stroke:rgb(255, 100, 255); stroke-width="2"'/>''')
f.write('</svg>\n')
f.close