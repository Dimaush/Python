from tkinter import *
import time
import random
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack(fill=BOTH)

def left(event):
   global vx
   vx=vx-1
def right(event):
   global vx
   vx=vx+1
   
def move(event):
   x=event.x
   y=event.y
   x1,x2,x3,x4=canvas.coords("ball") 
   canvas.move("ball", x-x1,0)
#def left(event):
    
#def left(event):
    
circle = canvas.create_oval(10,10,20,20, fill="#00f",tag="ball")
canvas.create_oval(100,10,110,20, fill="#0f0",tag="pet")

root.bind("a",left)
root.bind("d",right)
#canvas.bind("<Motion>",move)
#canvas.bind("<Down>",down)
#canvas.bind("<Up>",up)
vx=0
vy=0

while TRUE:
   x1,x2,x3,x4=canvas.coords("ball") 
  
   if x1<10: #left side
      vx=-vx
   if x3>490: #right side
      vx=-vx
   y1,y2,y3,y4=canvas.coords("pet")
   if (x1-y1)**2+(x2-y2)**2<100:
      canvas.delete("pet")
      x=random.randint(10,490)
      canvas.create_oval(x,10,x+10,20, fill="#0f0",tag="pet")
   canvas.move("ball",vx,vy)
   canvas.update()
   time.sleep(0.1)

root.mainloop()