import math
import random
tochki = [] 
def ygol1(a, b):
    x1, y1 = a
    x2, y2 = b
    dx = x2 - x1
    dy = y2 - y1

    hy = dy**2 + dx**2
    hy = math.sqrt(hy) 
    if hy == 0:
        return 0
    cfi = dx / hy
    rad = math.acos(cfi)
    if dy < 0: rad = -rad
    #grad = rad * 180 / math.pi
    return rad

def left(tochka):
    oldYgolmaxup = 0
    oldYgolminup = 10000000000
    oldYgolmaxdown = 0
    oldYgolmindown = -10000000000
    for p in tochki:
        ygol2 = ygol1(tochka, p)                                                        
        if ygol2 > oldYgolmaxup and ygol2 > 0:
            maxup = p
            oldYgolmaxup = ygol2
            oldleft = p
            maxleft = p
        elif ygol2 < oldYgolminup and ygol2 > 0:
   #         minup = ygol2
            oldYgolminup = ygol2
  #          oldleft = p
  #          maxleft = p
        elif ygol2 < oldYgolmaxdown and ygol2 < 0:
            maxdown = p
            oldYgolmaxdown = ygol2            
            oldleft = p
            maxleft = p
        elif ygol2 > oldYgolmindown and ygol2 < 0:
  #          mindown = ygol2
            oldYgolmindown = ygol2
 #           oldleft = p

 #           maxleft = p
    if oldYgolmaxdown == -7: return maxup
    if oldYgolmaxup == -7: return maxdown

    s1= oldYgolmaxdown - oldYgolminup + 2 * math.pi
    s2=oldYgolmaxup - oldYgolmindown       
    r = 0, 0
    if s1 <= math.pi: r = maxdown
    elif s2 <= math.pi: r = maxup


    f.write(f'''
    <line x1="{oldleft[0]}" y1="{oldleft[1]}" x2 = "{maxleft[0]}" y2 = "{maxleft[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''') 
    oldleft = p     
    tochki.remove(p)
    oldleft = p   
    return r

def left3(tochka):
    oldYgol = 4180
    oldleft = tochka
    for p in tochki:
        ygol2 = ygol1(tochka, p)
        if ygol2 < oldYgol:
            oldYgol = ygol2
            maxleft = p

            print(oldYgol)
                     
    f.write(f'''
    <line x1="{oldleft[0]}" y1="{oldleft[1]}" x2 = "{maxleft[0]}" y2 = "{maxleft[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')
    tochki.remove(p)

    oldleft = p 
   
    return oldleft 




#        if ygol2 < oldYgol:
#            oldYgol = ygol2
#            maxleft = p
#            print(oldYgol)
#            oldleft = p







f = open('left', 'w')
f.write('''
<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width='1000px' height="1000px">''')

  
for rfgr in range(100):
    gx = random.randint(250, 750)
    gy = random.randint(250, 750)
    tochki.append((gx, gy))
  





for p in tochki:
    x, y = p
    f.write(f'''
        <circle cx="{x}" cy="{y}" r="3" stroke="white" stroke-width="0" fill="blue" />''') 


    

le = left((0, 1000))
x, y = le

f.write(f'''
    <line x1="{0}" y1="{1000}" x2 = "{le[0]}" y2 = "{le[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')
f.write(f'''
    <line x1="{0}" y1="{1000}" x2 = "1000" y2 = "1000" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')    

le2 = left(le)
x, y = le2

f.write(f'''
    <line x1="{le[0]}" y1="{le[1]}" x2 = "{le2[0]}" y2 = "{le2[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')
f.write(f'''
    <line x1="{0}" y1="{le[1]}" x2 = "1000" y2 = "{le[1]}" style='stroke:rgb(207, 207, 207); stroke-width=3'/>''')  
le3 = left(le2)


f.write(f'''
    <line x1="{le2[0]}" y1="{le2[1]}" x2 = "{le3[0]}" y2 = "{le3[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')    

f.write(f'''
    <line x1="{0}" y1="{le2[1]}" x2 = "1000" y2 = "{le2[1]}" style='stroke:rgb(207, 207, 207); stroke-width=3'/>''')

le4 = left(le3)


f.write(f'''
    <line x1="{le3[0]}" y1="{le3[1]}" x2 = "{le4[0]}" y2 = "{le4[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')
f.write(f'''
    <line x1="{0}" y1="{le3[1]}" x2 = "1000" y2 = "{le3[1]}" style='stroke:rgb(207, 207, 207); stroke-width=3'/>''')
le5 = left(le4)


f.write(f'''
    <line x1="{le4[0]}" y1="{le4[1]}" x2 = "{le5[0]}" y2 = "{le5[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')    

f.write(f'''
    <line x1="{0}" y1="{le4[1]}" x2 = "1000" y2 = "{le4[1]}" style='stroke:rgb(207, 207, 207); stroke-width=3'/>''')


le6 = left(le5)


f.write(f'''
    <line x1="{le5[0]}" y1="{le5[1]}" x2 = "{le6[0]}" y2 = "{le6[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')

le7 = left(le6)
f.write(f'''
    <line x1="{0}" y1="{le[1]}" x2 = "1000" y2 = "{le[1]}" style='stroke:rgb(207, 207, 207); stroke-width=3'/>''')

f.write(f'''
    <line x1="{le6[0]}" y1="{le6[1]}" x2 = "{le7[0]}" y2 = "{le7[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')    



le4 = left(le3)


f.write(f'''
    <line x1="{le3[0]}" y1="{le3[1]}" x2 = "{le4[0]}" y2 = "{le4[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')

le5 = left(le4)


f.write(f'''
    <line x1="{le2[0]}" y1="{le2[1]}" x2 = "{le3[0]}" y2 = "{le3[1]}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')    










gfd = le


        













        
 

f.write('</svg>\n')           
f.close    



