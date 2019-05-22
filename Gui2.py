from tkinter import *
import time
import random as r
class Atom:
    def __init__(self, x=10, y=40, speed_x=None, speed_y=None, name=None, config=None):
        self.config = config
        self.pos = (x, y)
        self.speed = (speed_x, speed_y)
        self.radius =4# float(self.config['radius'])
        self.name = name
        self.color= '#%02x%02x%02x' %(
            r.randint(0,255),r.randint(0,255),r.randint(0,255))

    def __str__(self):
        return f"Atom \"{self.name}\"\n" \
            f"Pozycja: {self.pos}\n" \
            f"Prędkość: {self.speed}\n"

    def access_atom(self):
        return self.pos[0], self.pos[1], \
               self.speed[0], self.speed[1]

    def move(self, tickrate=20):
        self.pos = (
            self.pos[0] + self.speed[0] * (1 / int(tickrate)),
            self.pos[1] + self.speed[1] * (1 / int(tickrate)))
def Generuj():
    generacja=Generuj_Atomy()
    generuj.config(state=DISABLED)
    start.config(state=NORMAL)

class Generuj_Atomy():
    def __init__(self, particles=100):
        self.particules=list(range(particles))
        for ind, p_ in enumerate(self.particules):
            self.particules[ind]=Atom(x=r.randint(0,50),y=r.randint(0,(ramki//2)*50))
            x,y=self.particules[ind].pos
            rad=self.particules[ind].radius
            self.particules[ind].config=canva.create_oval(x-rad,y-rad,x+rad,y+rad)
            canva.itemconfig(self.particules[ind].config ,fill='#%02x%02x%02x' %(
            r.randint(0,255),r.randint(0,255),r.randint(0,255))
)
            
def START():
    canva.delete(red)
    start.config(state=DISABLED)
    
        
def STOP():
    stop.config(state=DISABLED)
    start.config(state=NORMAL)
okno = Tk()
ramki=20
okno.title('Entropia')
okno.geometry(str((ramki)*51+1)+'x'+str((ramki//2)*51+81))
frstart=Frame(master=okno,background='#F3E77F')
frstart.place(x=1, y=1, width=ramki*51, height=78)
canva=Canvas(master=okno, background='#F2FFCC')
canva.place(x=1, y=80, width=ramki*50, height=(ramki//2)*50)
canva.create_oval(10,80,10,80)


for i in range(1,ramki):
        canva.create_line(i*50,0,i*50,(ramki//2)*50,fill='#D9CCFF')
        red=canva.create_line(50,0,50,(ramki//2)*50,fill="red")
        
for i in range(1,ramki):
        canva.create_line(0,i*50,(ramki)*50,i*50,fill='#D9CCFF')
        
        
start=Button(master=frstart,text='START',command=START)
start.config(state=DISABLED)
start.place(x=(ramki*55-279)//2, y=40, width=98, height=20)
generuj=Button(master=frstart,text='Generuj Atomy',command=Generuj)
generuj.config(state=NORMAL)
generuj.place(x=1, y=40, width=100, height=20)
i=canva.create_oval(2,2,8,8)
canva.itemconfig(i,fill='#%02x%02x%02x' %(
            r.randint(0,255),r.randint(0,255),r.randint(0,255))
)


