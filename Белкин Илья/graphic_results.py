import math
from random import randint
mssx=[]
mssy=[]
rmas=[]
rrmas=[]
rput=[]
smas=[]
coords=int()
put=[]
f=open('Picture.svg','w')
f.write('<?xml version="1.0" encoding="utf-8"?>') 
f.write('\n')
f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200000px" height="200000px">')
f.write('\n')
for i in range(0,3):
    mssx.append(randint(250,750))
    mssy.append(randint(250,750))
    f.write(f'      <rect x="{mssx[i]}" y="{mssy[i]}" width="1.5" height="1.5" fill="red" stroke="blue" stroke-width="3" />')
    f.write('\n')
for j in range(1,361, 10):
    xs=2000
    a=2*math.pi/360*j
    oldP = -99999999999
    for i in range(0,len(mssx)):
        p=(mssx[i]*math.cos(a))+(mssy[i]*math.sin(a))
        if p > oldP:
            oldP=p
            coords = (mssx[i],mssy[i])
    put.append((coords,a))
for k in range(len(put)-1):
    r=math.sqrt((put[k-1][0][0]-put[k][0][0])**2+(put[k-1][0][1]-put[k][0][1])**2)
    rmas.append(r)
for g in range(len(rmas)):
    if rmas[g]!=0:
        rrmas.append(rmas[g])
        rput.append(put[g])
f.write(f'      <line x1="{0}" y1="{1000}" x2="{2000}" y2="{1000}" style="stroke:rgb(255,0,0);stroke-width:3;stroke:rgb(0,0,0)"/>')
f.write('\n')
h=0

while h<len(rrmas)-1:
    summ = 0
    while rrmas[h]<100 and h<len(rrmas)-1:
        summ+=rrmas[h]
        h+=1
    if summ != 0:
        smas.append(summ)
    else:
        smas.append(rrmas[h])
    h+=1
for l in range(len(smas)):
    f.write(f'      <line x1="{rput[l][1]*100}" y1="{1000}" x2="{rput[l][1]*100}" y2="{1000+smas[l]}" style="stroke:rgb(255,0,0);stroke-width:3;stroke:rgb(0,0,0)"/>')
    f.write('\n')
f.write('</svg>')
f.close()
amp=len(smas)
if amp>=4 and amp<=8:
    print('Square')
elif amp==1:
    print('Circle')
elif amp>=2 and amp<=3:
    print('Triangle')ыыы