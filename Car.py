from tkinter import *
root = Tk()
canvas = Canvas(root, width=250, height=100)
canvas.pack()

canvas.create_line( 60, 10,150, 10, width=2, fill="black")
canvas.create_line(150, 10,150, 50, width=2, fill="black")
canvas.create_line(150, 50,180, 50, width=2, fill="black")
canvas.create_line(180, 50,180, 80, width=2, fill="black")
canvas.create_line(180, 80,170, 80, width=2, fill="black")
canvas.create_line(170, 80,150, 60, width=2, fill="black")
canvas.create_line(150, 60,130, 80, width=2, fill="black")
canvas.create_line(130, 80, 80, 80, width=2, fill="black")
canvas.create_line( 80, 80, 60, 60, width=2, fill="black")
canvas.create_line( 60, 60, 40, 80, width=2, fill="black")
canvas.create_line( 40, 80, 30, 80, width=2, fill="black")
canvas.create_line( 30, 80, 30, 50, width=2, fill="black")
canvas.create_line( 30, 50, 60, 50, width=2, fill="black")
canvas.create_line( 60, 50, 60, 10, width=2, fill="black")

canvas.create_line( 70, 20,100, 20, width=2, fill="black")
canvas.create_line(100, 20,100, 70, width=2, fill="black")
canvas.create_line(100, 70, 90, 70, width=2, fill="black")
canvas.create_line( 90, 70, 70, 50, width=2, fill="black")
canvas.create_line( 70, 50, 70, 20, width=2, fill="black")
canvas.create_line( 75, 25, 95, 25, width=2, fill="black")
canvas.create_line( 95, 25, 95, 45, width=2, fill="black")
canvas.create_line( 95, 45, 75, 45, width=2, fill="black")
canvas.create_line( 75, 45, 75, 25, width=2, fill="black")
canvas.create_line( 95, 50, 95, 60, width=2, fill="black")

canvas.create_line(110, 20,140, 20, width=2, fill="black")
canvas.create_line(140, 20,140, 50, width=2, fill="black")
canvas.create_line(140, 50,120, 70, width=2, fill="black")
canvas.create_line(120, 70,110, 70, width=2, fill="black")
canvas.create_line(110, 70,110, 20, width=2, fill="black")
canvas.create_line(115, 25,135, 25, width=2, fill="black")
canvas.create_line(135, 25,135, 45, width=2, fill="black")
canvas.create_line(135, 45,115, 45, width=2, fill="black")
canvas.create_line(115, 45,115, 25, width=2, fill="black")
canvas.create_line(115, 50,115, 60, width=2, fill="black")

canvas.create_line( 60, 70, 70, 80, width=2, fill="black")
canvas.create_line( 70, 80, 60, 90, width=2, fill="black")
canvas.create_line( 60, 90, 50, 80, width=2, fill="black")
canvas.create_line( 50, 80, 60, 70, width=2, fill="black")

canvas.create_line(150, 70,160, 80, width=2, fill="black")
canvas.create_line(160, 80,150, 90, width=2, fill="black")
canvas.create_line(150, 90,140, 80, width=2, fill="black")
canvas.create_line(140, 80,150, 70, width=2, fill="black")

canvas.create_line( 30, 60, 25, 65, width=2, fill="black")
canvas.create_line( 25, 65, 30, 70, width=2, fill="black")
canvas.create_line( 20, 60, 15, 55, width=2, fill="black")
canvas.create_line( 20, 65, 15, 65, width=2, fill="black")
canvas.create_line( 20, 70, 15, 75, width=2, fill="black")

canvas.create_line(180, 65,200, 65, width=2, fill="black")
canvas.create_line(200, 65,200, 75, width=2, fill="black")
canvas.create_line(200, 75,180, 75, width=2, fill="black")

canvas.create_line(200, 70,215, 70, width=2, fill="black")
canvas.create_line(215, 70,215, 60, width=2, fill="black")
canvas.create_line(215, 60,210, 60, width=2, fill="black")
canvas.create_line(210, 60,210, 65, width=2, fill="black")
canvas.create_line(210, 65,225, 65, width=2, fill="black")
canvas.create_line(225, 65,225, 55, width=2, fill="black")
canvas.create_line(225, 55,220, 55, width=2, fill="black")
canvas.create_line(220, 55,220, 60, width=2, fill="black")
canvas.create_line(220, 60,235, 60, width=2, fill="black")

root.mainloop()