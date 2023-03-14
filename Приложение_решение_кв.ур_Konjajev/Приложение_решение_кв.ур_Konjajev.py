from tkinter import *

tekst="Квадратные уравнения"
aken=Tk()
aken.geometry("600x200")
aken.title(tekst)

nupp=Button(aken, 
            text="Решить",
            bg="green",
            fg="#0d010b",
            font="Chiller 20",
            activebackground="red",
            activeforeground="white",
            height=2,
            width=15)

pealkiri=Label(aken,
               text="Решение квадратного уравнения",
               bg="lightblue",
               fg="green",
               font="Chiller 20",
               height=1,
               width=50,
               justify=RIGHT)
tekst_kast=Entry(aken,
                 fg="Lightblue",
                 bg="Lightblue",
                 font="Chiller 20",
                 width=4)

tekst_kast1=Entry(aken,
                 fg="Lightblue",
                 bg="Lightblue",
                 font="Chiller 20",
                 width=4)


pealkiri.pack() 
tekst_kast.pack(pady=40,side=LEFT)
tekst_kast.pack(pady=40,side=LEFT)
nupp.pack(anchor=E)
aken.mainloop()
