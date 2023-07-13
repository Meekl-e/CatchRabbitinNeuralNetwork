'''a = 1
b = 0
while a > 0.000001:
    a = a/2
    b += a
print(b)    

def sum(a, b):
    return a + b
def mul(a, b):
    return a*b
print(sum(mul(22, 22), mul(33, 33)))

n = 1000   
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
print(fib(n))



n = int(input())
b = 1
a = 1
while a < n:
    b = b * a
    a = a + 1
    print(b, end=" ")
g = []
for b in range(100):
    g.append(100 - b - 1)
print(g) 
fam, man, otch, age = p1 


f = open('workfile', 'w')                fill = "{"#"+''.join([random.choice('ABCDEF0123456789') for gr in range(6)])}"
f.write('KYCOK CAXAPA AXAXAXAXAXXXA')

f.close()

import random

n = int(input())

i =[]
for f in range(n):
    b = random.randint(0, 10)
    b = b/10
    i.append(b)

print(i)
import random
n = int(input())
i = []
for g in range (n):
    for g in range (n):
        b = random.randint(0, 10)              {random.randint(1, 10000)}
        b = b/10
        i.append(b)
    print(i)
    i.clear()

import random
h = random.randint(1500, 15000)
c = random.randint(750, 7500)'''
import random
#f = open('worfle', 'w')
#f.write('''
#<?xml version="1.0" encoding="utf-8"?>
#<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width='10000px' height="10000px" fill = 'black'>''')
#f.write(f'''
#        <rect x ="250"  y = '250' width='500' height = '500' fill = "{"#"+''.join([random.choice('ABCDEF0123456789') for gr in range(6)])}" stroke = 'white' stroke-width='0'/>''')
   
#x, y = 0, 0
#n = 10000000
#l = 0
#points = 0
#for fh in range(n):
#    x = random.randint(1, 1000)
#    y = random.randint(1, 1000)
#    
#    
#    if y >= 250 and y <= 750 and x >= 250 and x <= 750: 
#        l += 1
#        f.write(f'''
#        <circle cx={x} cy={y} r="1" stroke="white" stroke-width="0" fill="{"#"+''.join([random.choice('ABCDEF0123456789') for gr in range(6)])}" />''')         
#if l >= 33:
#    print('кфадратgggg')
#else:
#    print('что странное')    


#for fgt in range(1):
#    f.write(f'''
#       <rect x ="250"  y = '250' width='500' height = '500' fill = "{"#"+''.join([random.choice('ABCDEF0123456789') for gr in range(6)])}" stroke = 'white' stroke-width='0'/>''')           {"#"+''.join([random.choice('ABCDEF0123456789') for gr in range(6)])}

tets = 0

from operator import index


ox = 0
oy = 1000

x5 = []
y5 = []
l = []
x = []
y = []
import math                

def ygol(a, b):
    x1, y1 = a
    x2, y2 = b

    b = x2 - x1
    c = y2 - y1
    a = c**2 + b**2
    a = a ** 0.5
    fi = b / a
    r = math.acos(fi)
    

#    if c < 0: r = -r  
    grad = r * 180 / math.pi

   # grad = int(grad)
    
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


















f = open('woryfle', 'w')
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


#w = min(l) 
#s = max(l) 
#indx = l.index(max(l))
#max = x[indx]
#may = y[indx]

 
indn = l.index(min(l))
mix = x[indn]
miy = y[indn]


ind = l.index(min(l))
#f.write(f'''
#        <circle cx="{mix}" cy="{miy}" r="{random.randint(3, 3)}" stroke="white" stroke-width="0" fill="red" />''')
 
f.write(f'''
        <circle cx="{ox}" cy="{oy}" r="{random.randint(3, 3)}" stroke="white" stroke-width="0" fill="black" />''')
#f.write(f'''
#        <line x1="{mix}" y1="{miy}" x2 = "{ox}" y2 = "{oy}" style='stroke:rgb(255, 0, 0); stroke-width=4'/>''')
f.write(f'''
        <line x1="0" y1="{oy}" x2 = "1000" y2 = "{oy}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')   
#f.write(f'''
#        <line x1="{max}" y1="{may}" x2 = "{ox}" y2 = "{oy}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')                           



h = -1
for efe in range(10):
    indx = l.index(max(l))    
    max2 = x[indx]
    may = y[indx]
    f.write(f'''
        <circle cx="{max2}" cy="{may}" r="{random.randint(5, 5)}" stroke="white" stroke-width="0" fill="orange" />''')
    f.write(f'''
        <line x1="{max2}" y1="{may}" x2 = "{ox}" y2 = "{oy}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')  


  



f.write(f'''
    <circle cx="{max}" cy="{may}" r="{random.randint(5, 5)}" stroke="white" stroke-width="0" fill="orange" />''')
f.write(f'''
    <line x1="{max}" y1="{may}" x2 = "{ox}" y2 = "{oy}" style='stroke:rgb(255, 0, 0); stroke-width=3'/>''')  


      
            
'''w = str(w)
mix = str(mix)
miy = str(miy)
max = str(max)
may = str(may)
s = str(s)




print('Мин.угол:' + w)
print('Корд мин угол по Х:' + mix)
print('Корд мин угол по Y:' + miy)
print('Макс.угол:'+ s)        
print('Корд макс угол по Х:' + max)
print('Корд макс угол по Y:' + may)'''





















f.write('</svg>\n')           
f.close
