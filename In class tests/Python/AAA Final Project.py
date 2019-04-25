#Python Final Project

import tkinter as tk

box = tk.Tk()
box.title("Final Project")
box.geometry("500x500")
box.resizable(0,0)

welcomelabel = tk.Label(box, text="Welcome to this shitty GUI")
welcomelabel.pack()




def Jeep_Choice():
    Cartype = "Jeep"
    JeepChoiceLabel = tk.Label(box, text="You chose a Jeep!")
    JeepChoiceLabel.pack()

def Suv_Choice():
    Cartype = "SUV"
    print("You chose an SUV!")

OptionSuv = tk.Button(box, text='SUV', width=25, command=Suv_Choice)

OptionJeep = tk.Button(box, text='Jeep', width=25, command=Jeep_Choice)

def Hey():
    Cartype = False
    Cartypelabel = tk.Label(box, text="Which type of car would you like?")
    Cartypelabel.pack()
    OptionJeep.pack()
    OptionSuv.pack()
        
    

def Main():
    #Put while loop here
    Cartype = False
    question = input("Do you want to buy a car?")
    if question == "Yes":
        Hey()
        

Main()




