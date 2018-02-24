from tkinter import *
import time
import random
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack(fill=BOTH)

text = canvas.create_text(250,250, text="You need get a ten ball.a,w,s,d-управление ", fill="purple", font=("Helvectica", "16"))

def left(event):
   global vx
   vx=vx-1
def right(event):
   global vx
   vx=vx+1
def up(event):
   global vy
   vy=vy-1
def down(event):
   global vy
   vy=vy+1
vy=0
vx=0
ochki=0
    
circle = canvas.create_oval(10,10,20,20, fill="#00f",tag="ball")
canvas.create_oval(100,10,110,20, fill="#0f0",tag="pet")

root.bind("a",left)
root.bind("d",right)
root.bind("s",down)
root.bind("w",up)


while TRUE:
   x1,x2,x3,x4=canvas.coords("ball") 
   a1,a2,a3,a4=canvas.coords("pet")
   if x1<0: #left side
      vx=-vx
   if x2<0:
      vy=-vy
   if x3>500:
      vx=-vx
   if x4>500:
      vy=-vy
      
   if (x1-a1)**2+(x2-a2)**2<10:  #consume pet
      canvas.delete("pet")
      x=random.randint(10,490)
      y=random.randint(10,490)
      canvas.create_oval(x,y,x+10,y+10, fill="#0f0",tag="pet")
      ochki=ochki+1
   if ochki > 9:
      canvas.delete(text)
      text = canvas.create_text(250,250, text="you win!", fill="purple", font=("Helvectica", "16"))
      
   
   canvas.move("ball",vx,vy)
   canvas.update()
   time.sleep(0.1)

root.mainloop()