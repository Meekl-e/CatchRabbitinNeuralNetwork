#Данная программа создает красивый рисунок из линий, а также множество точек, которые располагаются рандомно, но в точности внутри получившейся оболочки


#Импортируем библиотеки для дальнейшего использования в программе
import math
import random

f = open("risunak.svg", "w")
f.write('''<?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1500px" height="1500px">
            ''')

#Создаём список который в последствии будет наполняться
s = []
#Количество точек, можно заменить на ввод в консоли с помощью n = int(input(""))
n = 100
#Создаем минимальный p
p = -99999999

#Цикл для создания точек
for i in range(n):
    mcvX = random.randint(250, 950)
    mcvY = random.randint(250, 950)
    f.write(f'''
            <rect x="{mcvX}" y="{mcvY}" width="1" height="1" fill="blue" stroke="blue" stroke-width="1" />
         ''')
    mcv = mcvX, mcvY
    s.append(mcv)
x0, x1 = 0, 1500

#Цикл для рисования линий
for i in range(1, 361):
    a = 2*math.pi/360*i
    oldp = -10000000
    for point in s:
        p = point[0]*math.cos(a) + point[1]*math.sin(a)
        #Условие для изменения p
        if p > oldp:
            oldp = p
    p = oldp
    #Формулы
    y0 = (p - math.cos(a) * x0) / math.sin(a)
    y1 = (p - math.cos(a) * x1) / math.sin(a)
    f.write(f'''
            <line x1="{x0}" y1 ="{y0}" x2="{x1}" y2="{y1}" style="stroke:rgb(255, 255, 255);stroke-width:1;stroke:rgb(60, 190, 76)"/>
                ''')
    

a = math.pi / 4

y0 = (p - math.cos(a) * x0) / math.sin(a)
y1 = (p - math.cos(a) * x1) / math.sin(a)

#Для правильного выполнения программы нужно закрыть код рисования данной командой
f.write('''
</svg>\n
''')

#Закрываем файл для того чтобы прогррамма выполнялась успешно
f.close()
