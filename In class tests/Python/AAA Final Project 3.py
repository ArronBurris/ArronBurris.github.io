#Python Final Project

# Ask if they want to buy a car
# Ask what kind of car they want
# Give the different options aswell as the prices for them and a submit button
# Store user answer and the price in text file
# Ask what color they want based off of cartype
# Give the different options aswell as the prices for the colors
# Store user answer and the price in text file
# Read back their car decisions and price and ask if they are satisfied with their choice
# If yes then congradulate them on buying an overly expensive car
# If no then ask what they would like to change and re ask the question until satisfied.
# End program


import tkinter as tk

import sys

box = tk.Tk()
box.title("Final Project")
box.geometry("500x500")
box.resizable(0,0)

welcomelabel = tk.Label(box, text="Welcome to this shitty GUI")
welcomelabel.pack()

Buying_A_Car = False

class GUI:


    def Color_Choice_Page():
        JeepButton.pack_forget()
        SuvButton.pack_forget()
        TruckButton.pack_forget()
        SubmitButton.pack_forget()
        
        
    

    def Car_Type_Page():
        def Jeep_Choice():
            CarType = "Jeep"
            TypePrice = 10
            print("You chose a Jeep! The Jeep option will be $10.")

        def Suv_Choice():
            CarType = "Suv"
            TypePrice = 15
            print("You chose an Suv! The Suv option will be $15.")

        def Truck_Choice():
            CarType = "Truck"
            TypePrice = 5
            print("You chose a Truck! The Truck option will be $5.")
            
        JeepButton = tk.Button(box, text="Jeep", width=25, command=Jeep_Choice)
        SuvButton = tk.Button(box, text="Suv", width=25, command=Suv_Choice)
        TruckButton = tk.Button(box, text="Truck",width=25, command=Truck_Choice)
        SubmitButton = tk.Button(box, text="Submit",width=25, command=Color_Choice_Page)
        JeepButton.pack()
        SuvButton.pack()
        TruckButton.pack()
        SubmitButton.pack()
        
        

        


    while Buying_A_Car == False:
        Question = str(input("Would you like to purchase a car? y/n")).lower()
        if (Question == "yes" or Question == "y"):
            Buying_A_Car = True
            Car_Type_Page()
        elif (Question == "no" or Question == "n"):
            JustChecking = str(input("Are you sure? y/n")).lower()
            if (JustChecking == "yes" or JustChecking == "y"):
                sys.exit()
            elif (JustChecking == "no" or JustChecking == "n"):
                Buying_A_Car = True
                Car_Type_Page()
        else:
            print("Invalid response. Please answer yes or no")
            
        
        


