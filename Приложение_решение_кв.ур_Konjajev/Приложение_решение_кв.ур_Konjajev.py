from tkinter import *
from math import *
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")

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


raam = Tk()
raam.title("Шахматная доска")

canvas_width = 400
canvas_height = 400
canvas = Canvas(raam, width=canvas_width, height=canvas_height)
canvas.pack()
cell_width = int(canvas_width / 8)
cell_height = int(canvas_height / 8)
for row in range(8):
    for col in range(8):
        x1 = col * cell_width
        y1 = row * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        if (row + col) % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="black")
raam.mainloop()

"""
#1 флаг
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
"""
raam.mainloop()

































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