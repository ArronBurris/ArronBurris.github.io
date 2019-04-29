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

import sys

BuyingCar = False

Opening_Q = 0

CarType = None

TypePrice = 0

CarColor = None

ColorPrice = 0

TotalPrice = 0


def First_Q():
    print("hey")



def Main():
    First_Q()
    


while BuyingCar == False:
    Opening_Q = input("Hello! Would you like to buy a car?").lower()
    if (Opening_Q == "yes" or Opening_Q == "y"):
        BuyingCar = True
        Main()
    elif (Opening_Q == "no" or Opening_Q == "n"):
        Check = input("Are you sure?").lower()
        if (Check == "yes" or Check == "y"):
            print("Ok then leave ya cuck")
            sys.exit()
        elif (Check =="no" or Check == "n"):
            print("Stop wasting my time and buy a fuckin car")
            BuyingCar = True
            Main()
        else:
            print("Invalid response. Please answer with 'Yes' or 'No'")
                
                
                
Main()















    
    

        


