from msilib.schema import RadioButton
from tkinter import *

def valik(): #можно поставить значение от которогог зависити функция
    num=var.get()
    if num == 1:
        raam1 = Tk()
        raam1.title("Tahvel")
        tahvel1 = Canvas(raam1, 
                width=250, 
                height=150, 
                background="white")
        tahvel1.create_rectangle(0,0, 250,150,fill="#4cacc2")
        tahvel1.create_rectangle(0,50, 250,150,fill="yellow")
        tahvel1.create_rectangle(0,100, 250,150,fill="#4cacc2")
        tahvel1.create_polygon(0,0, 110,85, 0,150, fill="black")
        tahvel1.grid()
        raam1.mainloop()
    elif num == 2:
        raam2 = Tk()
        raam2.title("Tahvel")
        tahvel2 = Canvas(raam2, 
                width=250, 
                height=150, 
                background="white")
        tahvel2.create_rectangle(0,0, 250,150,fill="blue")
        tahvel2.create_rectangle(0,50, 250,150,fill="black")
        tahvel2.create_rectangle(0,100, 250,150,fill="white")
        tahvel2.grid()
        raam2.mainloop()
    elif num == 3:
        raam3 = Tk()
        raam3.title("Tahvel")
        tahvel3 = Canvas(raam3, 
                width=250, 
                height=150, 
                background="white")
        tahvel3.create_rectangle(0,0, 250,150,fill="white")
        tahvel3.create_rectangle(0,73, 250,150,fill="red")
        tahvel3.grid()
        raam3.mainloop()
def valik_2():
    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    lbox.insert(END,val1)
    lbox.insert(END,val2)
    lbox.insert(END,val3)
    if val1!="-": lbox.insert(END,val1)
    if val2!="-": lbox.insert(END,val2)
    if val3!="-": lbox.insert(END,val3)



aken=Tk()
aken.title("Erinevad nupud")
aken.geometry("200x300")
var=IntVar() #StringVar()

r1=Radiobutton(aken,text="Esimene",variable=var,value=1,command=valik)
r2=Radiobutton(aken,text="Teine",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text="Kolmas",variable=var,value=3,command=valik)
lbox=Listbox(aken,height=3,width=30) 

var1=StringVar()
var2=StringVar()
var3=StringVar()

c1=Checkbutton(aken,text="Esimene",variable=var1,onvalue="Esimene",offvalue="-",command=valik_2)
c2=Checkbutton(aken,text="Teine",variable=var2,onvalue="Teine",offvalue="-",command=valik_2)
c3=Checkbutton(aken,text="Kolmas",variable=var3,onvalue="Kolmas",offvalue="-",command=valik_2)
c1.deselect()
c2.deselect()
c3.deselect()

lbox.grid(row=0,column=0,columnspan=2)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)

c1.grid(row=1,column=1)
c2.grid(row=2,column=1)                                                                                                                                                                         
c3.grid(row=3,column=1)

aken.mainloop()




#1 флаг
raam1 = Tk()
raam1.title("Tahvel")
tahvel1 = Canvas(raam1, 
                width=250, 
                height=150, 
                background="white")
tahvel1.create_rectangle(0,0, 250,150,fill="#4cacc2")
tahvel1.create_rectangle(0,50, 250,150,fill="yellow")
tahvel1.create_rectangle(0,100, 250,150,fill="#4cacc2")
tahvel1.create_polygon(0,0, 110,85, 0,150, fill="black")
tahvel1.grid()
raam1.mainloop()


#2 флаг
raam2 = Tk()
raam2.title("Tahvel")
tahvel2 = Canvas(raam2, 
                width=250, 
                height=150, 
                background="white")
tahvel2.create_rectangle(0,0, 250,150,fill="blue")
tahvel2.create_rectangle(0,50, 250,150,fill="black")
tahvel2.create_rectangle(0,100, 250,150,fill="white")
tahvel2.grid()
raam2.mainloop()


#3 флаг

raam3 = Tk()
raam3.title("Tahvel")
tahvel3 = Canvas(raam3, 
                width=250, 
                height=150, 
                background="white")
tahvel3.create_rectangle(0,0, 250,150,fill="white")
tahvel3.create_rectangle(0,73, 250,150,fill="red")
tahvel3.grid()
raam3.mainloop()
