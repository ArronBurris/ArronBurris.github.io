#Python Final Project

import tkinter as tk

box = tk.Tk()
box.title("Final Project")
box.geometry("1000x1000")
box.resizable(0,0)

welcomelabel = tk.Label(box,text="Welcome")
welcomelabel.pack()


print("Hey what car u want")

def Hey():
    


        

Option1 = tk.Button(box, text='Option1', width=25, command=Hey)

Option1.pack()
