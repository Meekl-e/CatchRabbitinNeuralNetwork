import math
from pickletools import long4
from random import randint
mssx=[]
mssy=[]
put=[]

f=open('Picture_2.svg','w')
f.write('<?xml version="1.0" encoding="utf-8"?>') 
f.write('\n')
f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200000px" height="200000px">')
f.write('\n')
for i in range(0,3):
    mssx.append(randint(250,750))
    mssy.append(randint(250,750))
    f.write(f'      <rect x="{mssx[i]}" y="{mssy[i]}" width="1.5" height="1.5" fill="red" stroke="blue" stroke-width="3" />')
    f.write('\n')
def beast(mssx,mssy):
    perin=0
    xmin=min(mssx)
    ymin=min(mssy)
    xmax=max(mssx)
    ymax=max(mssy)
    perout=((xmax-xmin)+(ymax-ymin))*2
    for j in range(1,361, 10):
        a=2*math.pi/360*j
        oldP = -99999999999
        for i in range(0,len(mssx)):
            p=(mssx[i]*math.cos(a))+(mssy[i]*math.sin(a))
            if p > oldP:
                oldP=p
                coords = (mssx[i],mssy[i])
        put.append(coords)
    for h in range(0,len(put)):
        perin+=math.sqrt((put[h-1][0]-put[h][0])**2+(put[h-1][1]-put[h][1])**2)
    f.write(f'      <line x1="{xmin}" y1="{ymin}" x2="{xmin}" y2="{ymax}" style="stroke:rgb(255,0,0);stroke-width:1;stroke:rgb(0,0,0)"/>')
    f.write('\n')
    f.write(f'      <line x1="{xmin}" y1="{ymax}" x2="{xmax}" y2="{ymax}" style="stroke:rgb(255,0,0);stroke-width:1;stroke:rgb(0,0,0)"/>')
    f.write('\n')
    f.write(f'      <line x1="{xmax}" y1="{ymax}" x2="{xmax}" y2="{ymin}" style="stroke:rgb(255,0,0);stroke-width:1;stroke:rgb(0,0,0)"/>')
    f.write('\n')
    f.write(f'      <line x1="{xmax}" y1="{ymin}" x2="{xmin}" y2="{ymin}" style="stroke:rgb(255,0,0);stroke-width:1;stroke:rgb(0,0,0)"/>')
    f.write('\n')
    if perout/perin<1.2:
        return 'Bear'
    if perout/perin>=1.2 and perout/perin<=1.4:
        return 'Wolf'
    else:
        return 'Hare'
print(beast(mssx,mssy))
f.write('</svg>')
f.close()