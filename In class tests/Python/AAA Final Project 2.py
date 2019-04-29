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
Jeep = 0
SUV = 0
Truck = 0



       
def button_press():
    if Jeep:
        Cartype = "Jeep"
        Jeepbutton_pressLabel = tk.Label(box, text="You chose a Jeep!")
    elif SUV:
        Cartype = "Suv"
        Suvbutton_pressLabel = tk.Label(box, text="You chose an SUV!")
    elif Truck:
        Cartype = "Truck"
        Truckbutton_pressLabel = tk.Label(box, text="You chose a Truck!")
    print(Cartype)
    return Cartype

    




def Choice_main():
    Cartypelabel = tk.Label(box, text="Which type of car would you like?")
    Cartypelabel.pack()
    
    OptionJeep = tk.Button(box, text='Jeep', width=25, command=button_press)
    OptionJeep.pack()
    
    OptionSuv = tk.Button(box, text='SUV', width=25, command=button_press)
    OptionSuv.pack()
    
    OptionTruck = tk.Button(box, text='Truck', width=25, command=button_press)
    OptionTruck.pack()
    
    button_press()
        

        
def Main():
    Cartype = False
    question = input("Do you want to buy a car?")
    if question == "Yes":
        Choice_main()
        

Main()
"""class Color_Choice:

    def Color_Branches(self, Jeep, SUV, Truck):

    def Suv_Choice():
        Cartype = "SUV"
        SuvChoiceLabel = tk.Label(box, text="You chose an SUV!")
        
    def Truck_Choice():
        Catype = "Truck"
        TruckChoiceLabel = tk.Label(box, text="You chose a Truck!")"""


