import math
import random
from statistics import mean


tochki = [] 
tochkip = []
f = open('wory210fle', 'w')
f.write('''
<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width='400px' height="200px">
<rect x ="0"  y = '0' width='200' height = '200' fill = "rgb(0, 0, 0)" stroke = 'rgb(0, 255, 55)' stroke-width='1'/>''')
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
        if d > 0: ot += 1
        elif d <= 0: ot += 0

    if ot == 0:
        return 1
    else:
        return 0
d1 = 0       
f.write('''
        <line x1="200" y1="200" x2 = "400" y2 = "200" style='stroke:rgb(255, 0, 0); stroke-width=1'/>''')      
def analiz():
    d1 = 0  
    pcordsx = []
    pcordsy = []    
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
        pcordsx.append(pcord[0])
        pcordsy.append(pcord[1])
    lens2 = []
    for ef in range(len(pcordsx)):
        x1 = pcordsx[ef]
        y1 = pcordsy[ef]
        x2 = pcordsx[ef-1]
        y2 = pcordsy[ef - 1]
        len1 = math.sqrt((x2 - x1)**2 + (y2- y1) ** 2)
        if len1 != 0.0:
            f.write(f'''
        <circle cx="{x1}" cy="{y1}" r="2" stroke="white" stroke-width="0" fill="red" />''')
            d1 = d1 + len1
            f.write(f'''
        <line x1="{pcordsx[ef] + 200}" y1="200" x2 = "{pcordsx[ef] + 200}" y2 = "{len1}" style='stroke:rgb(255, 0, 0); stroke-width=1'/>''')

            lens2.append(len1)

    xmin = min(pcordsx)
    xmax = max(pcordsx)
    ymin = min(pcordsy)
    ymax = max(pcordsy)
    xp = xmax - xmin
    yp = ymax - ymin
    primol = (xp + yp) * 2
    cof = (primol - d1) / primol * 100
    crx = mean(pcordsx)
    cry = mean(pcordsx)
    cr = math.sqrt((crx ** 2 + xmin ** 2) + (cry ** 2 + ymin ** 2))
    pr = 2 * math.pi * cr
    cof2 = pr / primol
    print(cof2)
    if round(cof2) == 1:
        print('Круг')
    else:
        if cof >= 20:
            print('Треуголник')
        elif cof < 20:
            print('Прямоугольник')    

    #gf = str(len(lens2))
   # print('Кол-во точек:' + gf)


           
for rfgr in range(20):
    gx = random.randint(1, 200)
    gy = random.randint(1, 200)
    tochki.append((gx, gy))
analiz()     
for x in range(200):
    for y in range(200):
        g = toc(x, y)
        
        if g == 1:
            f.write(f'''
        <circle cx="{x}" cy="{y}" r="0.5" stroke="white" stroke-width="0" fill="rgb(0, 255, 55)" />''')
                   
f.write('</svg>\n')           
f.close    