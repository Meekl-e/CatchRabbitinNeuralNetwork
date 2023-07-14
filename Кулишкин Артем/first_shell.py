import math
import numpy
import random
#Функция вычисление угла
def Fi(a1, a2):
    xa = int(a1[0])
    ya = int(a1[1])
    xb = int(a2[0])
    yb = int(a2[1])
    dx = xb - xa
    dy = yb - ya
    #Нахождения гипотенузы, косинуса и после через функцию арккосинуса находим угол
    gip = (dx ** 2 + dy ** 2) ** 0.5
    cosin = dx / gip
    deg = numpy.arccos([cosin])
    if dy >= 0:
        itog = (180 * deg) / math.pi
    else:
        itog = - deg
        itog = (180 * itog) / math.pi
    if itog == 360:
        itog = 0
        return -1
    else:
        return itog
#подключение
f=open('shell', 'w')
f.write('''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000px" height="1000px">\n''')
#рандомный список точек
tochki = [(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)),
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)),
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)),
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)), 
(random.randint(3, 20), random.randint(3, 20)), (random.randint(3, 20), random.randint(3, 20)),
 (4, 20), (2, 2), (8, 4), (7, 5), (13, 9), (3, 5), (7, 7), (12, 5), (7, 4), (1, 7), (8, 17), (11, 9), (3, 15), (9, 13), (5, 3), (6, 9), (11, 8), (3, 4), (random.randint(3, 20), random.randint(3, 20))]
tochki = set(tochki)
tochki = list(tochki)
maxy = [0]
g = [(2, 5), (1, 5), (3, 5)]
maxe = []
for fer in tochki:
    if fer[1] > maxy[0]:
        maxy.append(fer[1])
        maxy.remove(maxy[0])
    elif fer[1] == maxy[0]:
        maxy.append(fer[1])
for ter in maxy:
    if ter < max(maxy):
        maxy.remove(ter)
for let in tochki:
    if let[1] == max(maxy):
        maxe.append((let[0], max(maxy)))
maxi = 0
lef = 0
toper = 0
mok = 0
endpoint = 0
mini = 0
#Функция всех левых точек
def Levo(tok):
    global toper
    global lef
    global maxi
    global tochki
    global mok
    global endpoint
    global mini
    maxi = 0
    mini = 0
    lef = 0
    maxdown = 0
    minup = 0
    mok = 0
    gav = 0
    kot = 0
    if tok in tochki:
        tochki.remove(tok)
    for i in range(len(tochki)):
        xy = tochki[i]
        xc = int(xy[0])
        yc = int(xy[1])
        #Запускаем функцию вычисления углов
        znak = Fi((tok), (xc, yc))
        if znak == -1:
            continue
        #Рисуем точку из списка
        f.write(f'''<rect x="{xc * 40}" y="{yc * 40}" width="5" height="5" fill="blue" stroke="black" stroke-width="2"/>\n''')
        if i == 0:
            maxi = znak
            lef = xy
        #Условия на определение самой левой точки
        elif znak > maxi:
            maxi = znak
            lef = xy
        if znak < mini:
            endpoint = xy
            mini = znak
        if toper == 1:
            if znak < 0:
                if maxdown == 0 or znak > maxdown:
                    maxdown = znak
                    gav = xy
            elif znak >= 0:
                if minup == 0 or znak < minup:
                    minup = znak
                    kot = xy
    if toper == 1:
        if minup == 0:
            lef = gav
        elif maxdown == 0:
            lef = kot
        else:
            s =  maxdown - minup + 2 * math.pi
            if s < math.pi:
                lef = gav
    #Рисований линий из нынешней точки в самую левую
    f.write(f'''<line  x1="{tok[0] * 40}" y1="{tok[1] * 40}" x2="{int(lef[0]) * 40}" y2="{int(lef[1]) * 40}" style="stroke:rgb(139,0,255);stroke-width:2"/>\n''')
    return lef, gav
#Запуск функции самых левых точек
print(Levo((1, 2)))
guf = lef
for j in range(14):
    if lef == endpoint:
        break
    if j > 1:
        toper = 1
    j - 1
    print(Levo((lef)))
    if j == 1:
        tochki.insert(0, guf)
#Рисование линии из последней точки в самую первую
f.write(f'''<line  x1="{endpoint[0] * 40}" y1="{(endpoint[1]) * 40}" x2="{int(guf[0]) * 40}" y2="{int(guf[1]) * 40}" style="stroke:rgb(139,0,255);stroke-width:2"/>\n''')
f.write(f'''<rect x="{1 * 40}" y="{2 * 40}" width="5" height="5" fill="blue" stroke="blue" stroke-width="6"/>\n''')
#f.write(f'''<line  x1="{lef[0] * 40}" y1="{lef[1] * 40}" x2="{int(guf[0]) * 40}" y2="{int(guf[1]) * 40}" style="stroke:rgb(255,244,79);stroke-width:2"/>\n''')
#'''print(Levo((9, 9)))
#print(maxi)'''
#"""f.write(f'''<rect x="{int(lef[0]) * 50}" y="{int(lef[1]) * 50}" width="5" height="5" fill="blue" stroke="black" stroke-width="3"/>\n''')"""
#"""f.write(f'''<line  x1="{1 * 50}" y1="{1 * 50}" x2="{int(prav[0]) * 50}" y2="{int(prav[1]) * 50}" style="stroke:rgb(168,228,160);stroke-width:4"/>\n''')
#f.write(f'''<rect x="{int(prav[0]) * 50}" y="{int(prav[1]) * 50}" width="5" height="5" fill="blue" stroke="black" stroke-width="3"/>\n''')"""
#f.write(f'''<line  x1="{1 * 50}" y1="{6 * 50}" x2="{1 * 50 + 950}" y2="{6 * 50}" style="stroke:rgb(0,0,0);stroke-width:2"/>\n''')
#f.write(f'''<line  x1="{6 * 50}" y1="{1 * 50}" x2="{6 * 50}" y2="{1 * 50 + 450}" style="stroke:rgb(0,0,0);stroke-width:2"/>\n''')"""
#print(f'{float(maxi)} - максимум')
f.write('\n</svg>')
f.close