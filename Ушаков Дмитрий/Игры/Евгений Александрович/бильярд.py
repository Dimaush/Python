from tkinter import * #Подключаем модуль Tkinter в наше приложение
import math
import random
root = Tk() #Производим инициализацию нашего графического интерфейса
canvas = Canvas(root, width=800, height=600) #Инициализируем Canvas размером 300х300 пикселей
canvas.pack() #Размещаем Canvas в окне нашего Tkinter-GUI
r_shar,r_lusa=10,12


class shar:
    def __init__(self,x,y,color):
        self.x,self.y,self.vx,self.vy,self.color,self.act,self.r=x,y,0,0,color,True,r_shar
        
class lusa:
    def __init__(self,x,y,r):
        self.x,self.y,self.r=x,y,r
    def draw(self):
        a=self.r
        canvas.create_oval(self.x-a,self.y-a,self.x+a,self.y+a,fill="black")

class table:
    def __init__(self,x,y,l,h,color,color1):
        self.x,self.y,self.h,self.l,self.c,self.c1=x,y,h,l,color,color1
        self.sh=[]
        self.lu=[lusa(self.x-l,self.y-h,r_lusa)]
        self.lu+=[lusa(self.x,self.y-h,r_lusa)]
        self.lu+=[lusa(self.x+l,self.y-h,r_lusa)]
        self.lu+=[lusa(self.x-l,self.y+h,r_lusa)]
        self.lu+=[lusa(self.x,self.y+h,r_lusa)]
        self.lu+=[lusa(self.x+l,self.y+h,r_lusa)]
    def draw(self):
        canvas.create_rectangle(self.x-self.l-r_lusa,self.y-self.h-r_lusa,self.x+self.l+r_lusa,self.y+self.h+r_lusa,fill=self.c1)
        canvas.create_rectangle(self.x-self.l,self.y-self.h,self.x+self.l,self.y+self.h,fill=self.c)
        for i in range (len(self.lu)):
            self.lu[i].draw()

class kiy:
    def __init__(self):
        self.n,self.v,self.a,self.l=0,0,0,50
    #def draw(self,stol):
        #canvas.create_line(stol.sh[self.n].x+round)

st=table(400,300,300,200,"green","brown")
st.draw()

root.mainloop() # Создаем постоянный цикл