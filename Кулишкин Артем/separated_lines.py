import math
import numpy
import random
f=open('lines', 'w')
f.write('''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000px" height="1000px">\n''')
tochki = []
for i in range(700):
    a = random.randint(300, 800)
    b = random.randint(300, 800)
    tochki.append((a, b))
tochki = set(tochki)
tochki = list(tochki)
alfa = 0
ber = 0 
while alfa <= 360:
    ber += 5
    alfa = 2 * math.pi / 360 * ber
    pmux = -99999999999
    for peg in tochki:
        f.write(f'''<rect x="{peg[0]}" y="{peg[1]}" width="5" height="5" fill="blue" stroke="black" stroke-width="1"/>\n''')
        pmax = peg[0] * math.cos(alfa) + peg[1] * math.sin(alfa)
        if pmax >= pmux:
            pmux = pmax
    print(pmux)
    p = pmux
    x1 = 0
    x2 = 1000
    y1 = (p - (math.cos(alfa) * x1)) / math.sin(alfa)
    y2 = (p - (math.cos(alfa) * x2)) / math.sin(alfa)
    f.write(f'''<line  x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:pink;stroke-width:2"/>\n''')
"""f.write(f'''<line  x1="{x2 + 2}" y1="{y1}" x2="{x2 + 2}" y2="{y2}" style="stroke:rgb(0,0,0);stroke-width:2"/>\n''')
f.write(f'''<line  x1="{x1}" y1="{y1 + 4}" x2="{x2}" y2="{y1 + 4}" style="stroke:rgb(0,0,0);stroke-width:2"/>\n''')"""



f.write('\n</svg>')
f.close