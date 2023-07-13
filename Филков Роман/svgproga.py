#Данная программа создает множество точек, и рисунок поверх, среди множества точек есть красные, те самые точки задающиеся рандомно


#Импортируем библиотеки для дальнейшего использования в программе
import random
import math

#Открываем файл формата SVG, для создания области рисования
f = open("workfile.svg", "w")
f.write('''<?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100px" height="100px">
            ''')


#P.1


#Создаём список который в последствии будет наполняться
s = []
#Количество точек, можно заменить на ввод в консоли с помощью n = int(input(""))
n = 5
#Создаем минимальный p
p = -99999999

#Цикл для создания точек
for i in range(n):
    pntX = random.randint(25, 75)
    pntY = random.randint(25, 75)
    f.write(f'''
            <rect x="{pntX}" y="{pntY}" width="0.1" height="0.1" fill="red" stroke="red" stroke-width="1" />
         ''')
    pnt = pntX, pntY
    s.append(pnt)

#Функция позволяющая пройтись по всем точкам
def analyse():
    pcords = []
    ocords = []
    #Создаем минимальные и максмальные x y
    
    for i in range(1, 361):
        a = 2*math.pi/360*i
        oldp = -100000000
        #Цикл для формулы p
        for point in s:
            p = point[0]*math.cos(a) + point[1]*math.sin(a)
            #Условие для изменения p
            if p > oldp:
                oldp = p
                pcord = point
        pcords.append(pcord)

    xmin= min(pcords, key = lambda p: pcords[0])
    xmax= max(pcords, key = lambda p: pcords[0])
    ymin= min(pcords[1], key = lambda p: pcords[0])
    ymax= max(pcords[1], key = lambda p: pcords[0])
    #Цикл в котором мы задаем x1, x2, y1, y2, после используя их для формулы нахождения
    for i in range (len(pcords)):
        pcords[i-1]
        x1, y1 = pcords[i]
        x2, y2 = pcords[i - 1]
        #Теорема пифагора в изменённом виде
        o = (math.sqrt((x2 - x1)**2)+((y2 - y1)**2))
        #Условие для добавления o в ocords, рабочее только при o>0
        if o > 0:
            ocords.append(o)
    #Распечатываем в консоли питона ocords, в котором будет находиться 5 элементов >0
    print(ocords)

analyse()

#P.2


#Создаем функцию для проверки точек
def chpnt(x, y):
    dists = []
    #Цикл для переодичности создания линий
    for i in range(1, 361, 20):
        a = 2*math.pi/360*i
        oldp = -100000000
        #Цикл для высчитывания p
        for point in s:
            p = point[0]*math.cos(a) + point[1]*math.sin(a)
            #Условие для изменения p
            if p > oldp:
                oldp = p
        p = oldp
        #Формула
        d = x*math.cos(a) + y*math.sin(a) - p
        p = oldp
        x0, x1 = 0, 1000
        y0 = (p - math.cos(a) * x0) / math.sin(a)
        y1 = (p - math.cos(a) * x1) / math.sin(a)
        f.write(f'''
            <line x1="{x0}" y1 ="{y0}" x2="{x1}" y2="{y1}" style="stroke:rgb(255, 255, 255);stroke-width:1;stroke:rgb(60, 190, 76)"/>
                ''')
    #Условия для формулы d
    if d > 0:
        dists.append(1)
    else:
        dists.append(0)
    if sum(dists)==0:
        return 1
    else:
        return 0


#P.3


for x in range(100):
    for y in range(100):
        if chpnt(x, y) == 1:
            f.write(f'''
            <circle cx="{x}" cy="{y}" r="0.5" fill="black"  />
            ''')


Per0 = ()
Per1 = ()


#Для правильного выполнения программы нужно закрыть код рисования данной командой
f.write('''
</svg>\n
''')

#Закрываем файл для того чтобы прогррамма выполнялась успешно
f.close()
