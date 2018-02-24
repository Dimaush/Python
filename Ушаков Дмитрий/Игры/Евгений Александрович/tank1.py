from tkinter import *
from math import *
import time
import random
class bot:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ang=0
        self.bul=0
class bullet:
    def __init__(self,x,y,sp,ang,id):
        self.x=x
        self.y=y
        self.ang=ang
        self.sp=sp
        self.id=id
class tank :
    def __init__(self,x,y,):
        self.x=x
        self.y=y
        self.ang=0
        self.sp=0
        self.bul=0
        self.tw=0
    
        

root=Tk()
scr_x,scr_y=500,500
canv=Canvas(root, height=scr_x, width=scr_y, bg="green")
canv.pack()


def angle_point(x1,y1,x2,y2):
    x,y=x2-x1,y2-y1
    r=(x**2+y**2)**0.5
    if r==0: angle=0
    else:
        angle=acos(x/r)/pi*180
    if y<0: angle*=-1
    angle=(angle+360)%360
    return angle

def draw(b1,pu1,t1,bul):
    global bot_number
    canv.delete("all")
    canv.create_polygon(t1.x+25*cos((t1.ang+38)/180*pi),t1.y+25*sin((t1.ang+38)/180*pi),t1.x+30*cos((t1.ang+150)/180*pi),t1.y+30*sin((t1.ang+150)/180*pi),t1.x+30*cos((t1.ang+210)/180*pi),t1.y+30*sin((t1.ang+210)/180*pi),t1.x+25*cos((t1.ang+322)/180*pi),t1.y+25*sin((t1.ang+322)/180*pi),outline="black",fill="grey")
    canv.create_line(t1.x,t1.y,t1.x+35*cos((t1.tw)/180*pi), t1.y+35*sin((t1.tw)/180*pi), fill="black",width=3)
    canv.create_oval(t1.x-10,t1.y-10,t1.x+10,t1.y+10,outline="black",fill="grey")
    if t1.bul==2:   
        canv.create_oval(bul.x-5,bul.y-5,bul.x+5,bul.y+5,outline="red",fill="orange")
    # shot phase 2 - normal bullet fly
    elif 30>t1.bul>2:
        canv.create_oval(bul.x-1,bul.y-1,bul.x+1,bul.y+1,outline="red",fill="orange")
    elif t1.bul==30: 
        canv.create_oval(bul.x-15,bul.y-15,bul.x+15,bul.y+15,outline="red",fill="orange")
    for i in range (bot_number):
        canv.create_line(b1[i].x,b1[i].y,b1[i].x+35*cos((b1[i].ang)/180*pi), b1[i].y+35*sin((b1[i].ang)/180*pi), fill="black",width=3)
        canv.create_oval(b1[i].x-10,b1[i].y-10,b1[i].x+10,b1[i].y+10,outline="black",fill="grey")
    #if bot_bul_st>0:
    canv.create_oval(pu1.x-5,pu1.y-5,pu1.x+1,pu1.y+1,outline="red",fill="orange")
    
    canv.update()

def shot(event):
    global t1
    if t1.bul==0 and ( t1.x>3 or t1.y>3 or t1.x<scr_x-3 or t1.y<scr_y-3):
        t1.bul=1
def t_tow (event):
    global mouse_x,mouse_y
    mouse_x,mouse_y=event.x,event.y
 
def t_ccw(event):
    global t1
    t1.ang+=5
    t1.ang= t1.ang %360
    #t1.sp=0
def t_cw(event):
    global t1
    t1.ang-=5
    t1.ang= t1.ang %360
    #t1.sp=0
def s_up(event):
    global t1
    t1.sp+=1

def s_down(event):
    global t1
    t1.sp-=1
# initialization 
angt1=0
spt1=0
ang_tw=0
angle=0
bul_status=0
bul_x,bul_y,ang_bul=0,0,0
sp_bul=5
bot_number=25
t1=tank(100,100)
mouse_x,mouse_y=t1.x,t1.y
b1=[]
bul=bullet(0,0,sp_bul,t1.tw,id(t1))
for i in range(bot_number):
    x=bot(random.randint(20,480),random.randint(20,480))
    b1+=[x]

#list of events
root.bind ("<d>", t_ccw)
root.bind("<a>", t_cw)
root.bind("<w>", s_up)
root.bind("<s>", s_down)
root.bind("<Motion>",t_tow)
root.bind("<space>",shot)
root.bind("<Button-1>",shot)

while 1:
    #speed limits
    if t1.sp>3: t1.sp=3
    if t1.sp<-1: t1.sp=-1
    #move tank
    t1.x+=t1.sp*cos(t1.ang/180*pi)
    t1.y+=t1.sp*sin(t1.ang/180*pi)
    #borgers
    if t1.x<3 or t1.y<3 or t1.x>scr_x-3 or t1.y>scr_y-3: t1.sp=0
    #tower rotation
    angle=angle_point(t1.x,t1.y,mouse_x,mouse_y)
    #rotate tower to mouse direction
    if 180>angle-t1.tw>6 or 180>360+angle-t1.tw>5: t1.tw+=6
    elif abs(angle-t1.tw)>6 : t1.tw-=6
    t1.tw=(t1.tw+360) %360
    #shot phase1
    if t1.bul==1: 
        bul=bullet(t1.x+35*cos((t1.tw)/180*pi),t1.y+35*sin((t1.tw)/180*pi),sp_bul,t1.tw,id(t1))
        t1.bul=2
    #shot phase 2
    elif t1.bul==2:
        t1.bul=3
    # shot phase 3 - normal bullet fly
    elif 30>t1.bul>2:
        bul.x+=bul.sp*cos(t1.tw/180*pi)
        bul.y+=sp_bul*sin(t1.tw/180*pi)
        t1.bul+=1
        if bul.x<3 or bul.y<3 or bul.x>scr_x-3 or bul.y>scr_y-3: t1.bul=0
        
    else: t1.bul=0  
    # rotate bot to tank    
    for i in range(bot_number):
        b1[i].ang=angle_point(b1[i].x,b1[i].y,t1.x,t1.y)
    #bot shootint
    i=1
    if b1[i].bul==0:
        pu1=bullet(b1[i].x+35*cos((b1[i].ang)/180*pi),b1[i].y+35*sin((b1[i].ang)/180*pi),sp_bul,b1[i].ang,id(b1[i]))
        b1[i].bul=1
    elif pu1.x<3 or pu1.y<3 or pu1.x>scr_x-3 or pu1.y>scr_y-3: 
        b1[i].bul=0
    else: 
        pu1.x,pu1.y=pu1.x+pu1.sp*cos(pu1.ang/180*pi),pu1.y+pu1.sp*sin(pu1.ang/180*pi)
    #hit tank
    
        x1,y1,x2,y2,x3,y3,x4,y4=  t1.x+25*cos((t1.ang+38)/180*pi),t1.y+25*sin((t1.ang+38)/180*pi),t1.x+30*cos((t1.ang+150)/180*pi),t1.y+30*sin((t1.ang+150)/180*pi),t1.x+30*cos((t1.ang+210)/180*pi),t1.y+30*sin((t1.ang+210)/180*pi),t1.x+25*cos((t1.ang+322)/180*pi),t1.y+25*sin((t1.ang+322)/180*pi)
        a1=(pu1.x-x1)*(y2-y1)-(x2-x1)*(pu1.y-y1)
        a2=(pu1.x-x2)*(y3-y2)-(x3-x2)*(pu1.y-y2)
        a3=(pu1.x-x3)*(y4-y3)-(x4-x3)*(pu1.y-y3)
        a4=(pu1.x-x4)*(y1-y4)-(x1-x4)*(pu1.y-y4)
        if a1<=0 and a2<=0 and a3<=0 and a4<=0:
            b1[i].bul=0
    
    draw(b1,pu1,t1,bul)
    time.sleep(0.1)
root.mainloop()