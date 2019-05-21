from tkinter import *
def Generuj_Atomy():
    generuj.config(state=DISABLED)   
    start.config(state=NORMAL)
def START():
    start.config(state=DISABLED)
    stop.config(state=NORMAL)
def STOP():
    stop.config(state=DISABLED)
    start.config(state=NORMAL)
okno = Tk()
ramki=20
okno.title('Entropia')
okno.geometry(str(ramki*55-79)+'x'+str((ramki//2)*55+80))
frstart=Frame(master=okno,background='#F3E77F')
frstart.place(x=1, y=1, width=ramki*55-77, height=104)
for i in range(1,ramki+1):
    for j in range(1,(ramki//2)+1):
        if i==1:
            fr=Frame(master=okno,
                          background='#D5E88F')
        else:
            fr=Frame(master=okno,
                          background='#889E9D')
        fr.place(x=(i+50*(i-1)), y=105+j+50*(j-1), width=50, height=50)
        
start=Button(master=frstart,text='START',command=START)
start.config(state=DISABLED)
start.place(x=(ramki*55-279)//2, y=80, width=98, height=20)
generuj=Button(master=frstart,text='Generuj Atomy',command=Generuj_Atomy)
generuj.config(state=NORMAL)
generuj.place(x=1, y=80, width=98, height=20)
stop=Button(master=frstart,text='STOP',command=STOP)
stop.config(state=DISABLED)
stop.place(x=(ramki*55-79)//2, y=80, width=98, height=20)
