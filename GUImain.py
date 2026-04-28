"""
This is an example of a GUI and a class
using Tkinter and PointMass class
<<<-
o<:O)
"""
import tkinter as tk

root= tk.Tk()
root.title("Santasoft and amigo")
root.geometry("400x400")
#frame according to our design, 2 side by side and one below
frameInfo= tk.LabelFrame(root,bg="white")
frameCanvas= tk.Frame(root, bg="blue")
frameUpdate= tk.Frame(root,bg="green")

frameInfo.pack(side="left")
frameCanvas.pack(side="right")
frameUpdate.pack(side="bottom")

#widgets on the info thingy
tk.Label(frameInfo, text='Mass', justify="left", anchor="w").grid(row=0,column=0)
e1=tk.Entry(frameInfo, width=10,).grid(row=0, column=1)
tk.Label(frameInfo, text='Init Vol',justify="left").grid(row=1,column=0)
e2=tk.Entry(frameInfo, width=10,justify="left").grid(row=1, column=1)
tk.Label(frameInfo, text='location (x,y)',justify="left").grid(row=2,column=0)
e3=tk.Entry(frameInfo, width=10,justify="left").grid(row=2, column=1)

#widget on canvas_frame (probably just the canvas)
c= tk.Canvas(frameCanvas, width=200, height=200, bg="black")
c.grid(row=0, column=0)
#drawing
x, y= 25,50
d=30
face= c.create_oval(x, y,55,80, fill="red")


#widgets on particle update
l1=tk.Label(frameUpdate, text="Hello bud part", ).grid(row=0,column=0)
l2=tk.Label()



root.mainloop()