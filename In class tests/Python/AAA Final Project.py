#Python Final Project

# Ask if they want to buy a car
# Ask what kind of car they want
# Give the different options aswell as the prices for them
# Store user answer and the price in text file
# Ask what color they want based off of cartype
# Give the different options aswell as the prices for the colors
# Store user answer and the price in text file
# Read back their car decisions and price and ask if they are satisfied with their choice
# If yes then congradulate them on buying an overly expensive car
# If no then ask what they would like to change and re ask the question until satisfied.
# End program

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
    JeepChoiceLabel.pack(padx=5, pady=10, side=tk.LEFT)

def Suv_Choice():
    Cartype = "SUV"
    SubChoiceLabel = tk.Label(box, text="You chose an SUV!")
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




