import math
from random import randint
mssx=[]
mssy=[]
f=open('Picture.xml','w')
f.write('<?xml version="1.0" encoding="utf-8"?>') 
f.write('\n')
f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="2000px" height="2000px">')
f.write('\n')
for i in range(0,1000):
    mssx.append(randint(250,750))
    mssy.append(randint(250,750))
    f.write(f'      <rect x="{mssx[i]}" y="{mssy[i]}" width="1.5" height="1.5" fill="red" stroke="blue" stroke-width="3" />')
    f.write('\n')
xs=500
for j in range(1,361):
    xs=2000
    a=2*math.pi/360*j
    oldP = -99999999999
    for i in range(0,len(mssx)):
        p=(mssx[i]*math.cos(a))+(mssy[i]*math.sin(a))
        if p > oldP:
            oldP=p
    p=oldP
    yf=p/math.sin(a)
    ys=(p-math.cos(a)*xs)/math.sin(a)
    f.write(f'      <line x1="0" y1="{yf}" x2="{xs}" y2="{ys}" style="stroke:rgb(255,0,0);stroke-width:1;stroke:rgb(0,0,0)"/>')
    f.write('\n')
f.write('</svg>')
f.close()