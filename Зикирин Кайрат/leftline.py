import random
from operator import index
import math 


h = -1
ox = 0
oy = 1000
tets = 0
x5 = []
y5 = []
l = []
x = []
y = []
i = []
o=[]
u=[]
def ygol(a, b):
    x1, y1 = a
    x2, y2 = b
    b = x2 - x1
    c = y2 - y1
    a = c**2 + b**2
    a = a ** 0.5
    fi = b / a
    r = math.acos(fi)
    grad = r * 180 / math.pi    
    tets = round(grad, 15)
    tets = round(grad, 14)
    tets = round(grad, 13)
    tets = round(grad, 12)
    tets = round(grad, 11)
    tets = round(grad, 10)
    tets = round(grad, 9)
    tets = round(grad, 8)
    tets = round(grad, 7)
    tets = round(grad, 6)
    tets = round(grad, 5)
    tets = round(grad, 4)
    tets = round(grad, 3)
    tets = round(grad, 2)
    tets = round(grad, 1)
    tets = round(grad)
    tets = int(tets)  
    l.append(tets)
    x.append(x2)
    y.append(y2) 







f = open('leftline', 'w')
f.write('''
<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width='1000px' height="1000px">''')

for fgghht in range(100):
    h = random.randint(250, 750)
    k = random.randint(250, 500)
    f.write(f'''
        <circle cx="{h}" cy="{k}" r="3" stroke="white" stroke-width="0" fill="blue" />''')               
  
    a = (ox, oy)  
    b = (h, k)  
    ygol(a, b)
indx = l.index(max(l))    
maxy = x[indx]
may = y[indx]    

    

f.write(f'''
        <circle cx="{ox}" cy="{oy}" r="{random.randint(3, 3)}" stroke="white" stroke-width="0" fill="black" />''')
f.write(f'''
        <line x1="0" y1="{oy}" x2 = "1000" y2 = "{oy}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')

f.write(f'''
    <circle cx="{maxy}" cy="{may}" r="{random.randint(5, 5)}" stroke="white" stroke-width="0" fill="orange" />''')
f.write(f'''
    <line x1="{maxy}" y1="{may}" x2 = "{ox}" y2 = "{oy}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')          
n = 1
for efe in range(10):
    l.remove(max(l)) 
    x.pop(indx) 
    y.pop(indx)  
    indx = l.index(max(l))    
    max2 = x[indx]
    may = y[indx]
    ox = max2
    oy = may

    l.clear()
    for rg in range(99-n):
        xx = x[n]
        yy = y[n]    
        a = (ox, oy)
        b = (xx, yy)
        ygol(a, b)
    f.write(f'''
        <circle cx="{max2}" cy="{may}" r="{random.randint(5, 5)}" stroke="white" stroke-width="0" fill="orange" />''')
    f.write(f'''
        <line x1="{max2}" y1="{may}" x2 = "{ox}" y2 = "{oy}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')    
        
   
        


f.write('</svg>\n')           
f.close    





