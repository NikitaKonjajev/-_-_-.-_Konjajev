from tkinter import *

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
               font="Algerian 22", #Algerian
               height=2,
               width=2)

pealkiri3=Label(aken, #Пишет =0
               text="=0",
               fg="green",
               font="Algerian 22", #Algerian
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
