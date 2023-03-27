from tkinter import font
from tkinter import *
def Svetofor(aken):
    aken.create_line(0,0,  0,400,  width=330 , fill="#a3a7ad")
    suur_font = font.Font(family='Algerian', size=20, weight='bold')
    aken.create_text(40, 0, text="Valgusfoor", font=suur_font, anchor=NW)
    aken.create_line(60,50,  100,50,  width=40 , fill="red")
    aken.create_line(60,100,  100,100,  width=40 , fill="yellow")
    aken.create_line(60,150,  100,150,  width=40 , fill="green")
    aken.create_line(80 ,180,  80,300,  width=8 , fill="black")
    aken.create_line(30,310,  140,310,  width=4 , fill="black")

def Svetofor1(aken):
    aken.create_line(0,0,  0,400,  width=330 , fill="#a3a7ad")
    suur_font = font.Font(family='Algerian', size=20, weight='bold')
    aken.create_text(40, 0, text="Valgusfoor", font=suur_font, anchor=NW)
    aken.create_line(60,50,  100,50,  width=40 , fill="yellow")
    aken.create_line(60,100,  100,100,  width=40 , fill="yellow")
    aken.create_line(60,150,  100,150,  width=40 , fill="yellow")
    aken.create_line(80 ,180,  80,300,  width=8 , fill="black")
    aken.create_line(30,310,  140,310,  width=4 , fill="black")


