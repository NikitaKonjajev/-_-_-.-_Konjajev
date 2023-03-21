from tkinter import *
from math import *
from random import *
#1 флаг
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, 
                width=600, 
                height=600, 
                background="white")
tahvel.create_rectangle(25,50, 250,150,fill="#4cacc2")
tahvel.create_rectangle(25,100, 250,150,fill="yellow")
tahvel.create_rectangle(25,200, 250,150,fill="#4cacc2")
#2 флаг
tahvel.create_rectangle(500,50, 260,150,fill="blue")
tahvel.create_rectangle(500,100, 260,150,fill="black")
tahvel.create_rectangle(500,200, 260,150,fill="white")
#тругольник на флаге
tahvel.create_polygon(25,50, 110,125, 25,200, fill="black")
#3 флаг 
tahvel.create_rectangle(25,250,  250,300,fill="white")
tahvel.create_rectangle(25,350,  250,300,fill="red")
tahvel.grid()
raam.mainloop()


#квадраты
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, 
                width=600, 
                height=600, 
                background="white")

x0=0
y0=0
x1=600
y1=600
a=300
r=(a**2+a**2)**(1/2)
p=(a-r)
for i in range(12):
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    tahvel.create_rectangle(x0,y0,x1,y1,width=1,outline="blue",fill="red")
    tahvel.create_oval(x0,y0,x1,y1,width=1,outline="blue",fill="yellow")
    p=r-a 
    r=r-p
    a=((r)*sqrt(2))/2
tahvel.grid()
raam.mainloop()

#шахматы
raam3 = Tk()
raam3.title("Шахматная доска")
Canvas(raam3, 
       width=500, 
       height=500, 
       background="white")
canvas = Canvas()
width=250
height=250
width1=int(width/8)
height1=int(height/8)
for row in range(8):
    for col in range(8):
        x1=col*width1
        y1=row*height1
        x2=x1+width1
        y2=y1+height1
        if (row+col) % 2 == 0:
            canvas.create_rectangle(x1,y1,x2,y2,fill="white")
        else:
            canvas.create_rectangle(x1,y1,x2,y2,fill="black")
canvas.pack()
raam3.mainloop()

#круг
colors=["black",
        "cyan",
        "magenta",
        "red",
        "blue",
        "gray",
        "yellow",
        "green",
        "lightblue",
        "pink",
        "gold"]
raam2=Tk()
raam2.title("Ringid")
tahvel2=Canvas(raam2,width=600,height=600,bg="white")
x=0
y0=0
x1=600
y2=600
p=5
for i in range(55):
    x0+=p 
    y0+=p
    x1-=p 
    y1-=p 
    tahvel2.create_oval(x0,y0,x1,y1, fill=choice(colors))
    #sleep(1)
tahvel2.grid()
raam2.mainloop()








































"""
tekst="Квадратные уравнения"
aken=Tk()
aken.geometry("600x200")
aken.title(tekst)

pealkiri=Label(aken, #текст сверху "Решение квадратного уравнения"
               text="Решение квадратного уравнения",
               bg="lightblue",
               fg="green",
               font="Algerian 20",
               height=1,
               width=50,
               justify=RIGHT)

nupp=Button(aken, #кнопка решить 
            text="Решить",
            bg="green",
            fg="black",
            font="Chiller 20",
            activebackground="red",
            activeforeground="white",
            height=2,
            width=10)

nupp2=Button(aken, #кнопка решение
            text="Решение",
            bg="yellow",
            fg="black",
            font="Algerian 10",
            height=3,
            width=52)

pealkiri1=Label(aken, #пишет x**2
               text="x**2+",
               fg="green",
               font="Algerian 22", 
               height=5,
               width=5)

pealkiri2=Label(aken, #пишет x+
               text="x+",
               fg="green",
               font="Algerian 22", 
               height=2,
               width=2)

pealkiri3=Label(aken, #Пишет =0
               text="=0",
               fg="green",
               font="Algerian 22", 
               height=2,
               width=2)

tekst_kast=Entry(aken, #окно куда писть 1
                 fg="Lightblue",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=4)

tekst_kast1=Entry(aken, #окно куда писать 2
                 fg="Lightblue",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=4)

tekst_kast2=Entry(aken, #окно куда писать 3
                 fg="Lightblue",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=3,
                 justify=LEFT)

pealkiri.pack() 
nupp2.pack(side=BOTTOM)
tekst_kast.pack(side=LEFT)
pealkiri1.pack(side=LEFT)
tekst_kast1.pack(side=LEFT)
pealkiri2.pack(side=LEFT)
tekst_kast2.pack(side=LEFT)
pealkiri3.pack(side=LEFT)
nupp.pack(side=LEFT)


aken.mainloop()
"""