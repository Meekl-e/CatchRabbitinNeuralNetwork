import random
import math
gg=[]
f=open('Yar127', 'w')
f.write('''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="2000px" height="1000px">''')
for i in range(99999):
    x1 = random.randint(0, 2000)
    y1 = random.randint(0, 2000)
    x2 = random.randint(0, 2000)
    y2 = random.randint(0, 2000)
    b = x2 - x1
    c = y2 - y1
    h = c**2+b**2
    h = h**0.5
    fi = b / h
    r = math.acos(fi)
    if c < 0: r = -r
    graduci = r*180/math.pi
    graduci=int(graduci)
    gg.append(graduci)
    colors = ['red', 'black', 'green', 'blue']
    qwerty = random.choice(colors)
    yw = random.randint(150, 255)
    cn = random.randint(150, 255)
    f.write(f'''<line x1="{x1}" y1="{y1}" x2="{2000}" y2="{500}" style='stroke:rgb({random.randint(0, 0)}, {random.randint(0, 0)}, {random.randint(150, 255)}); stroke-width="2"'/>''')
    f.write(f'''<line x1="{x1}" y1="{y1}" x2="{0}" y2="{500}" style='stroke:rgb({random.randint(150, 255)}, {random.randint(0, 0)}, {random.randint(0, 0)}); stroke-width="2"'/>''')
    f.write(f'''<line x1="{x1}" y1="{y1}" x2="{1000}" y2="{500}" style='stroke:rgb({random.randint(0, 0)}, {random.randint(150, 255)}, {random.randint(0, 0)}); stroke-width="2"'/>''')
    f.write(f'''<line x1="{x1}" y1="{y1}" x2="{500}" y2="{500}" style='stroke:rgb({yw}, {yw}, {random.randint(0, 0)}); stroke-width="2"'/>''')
    f.write(f'''<line x1="{x1}" y1="{y1}" x2="{1500}" y2="{500}" style='stroke:rgb({random.randint(0, 0)}, {cn}, {cn}); stroke-width="2"'/>''')
    f.write(f'''<circle cx="{x1}" cy="{y1}" r="0" fill="{qwerty}" stroke="{qwerty}" stroke-width="0" />''')
    f.write(f'''<circle cx="{x2}" cy="{y2}" r="0" fill="{qwerty}" stroke="{qwerty}" stroke-width="0" />''')
f.write('</svg>\n')
f.close
mc=max(gg)
mcc=min(gg)
print(mc, mcc)