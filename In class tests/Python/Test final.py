#Python Final Project

# Ask if they want to buy a car
# Ask what kind of car they want
# Give the different options aswell as the prices for them and a submit button
# Store user answer and the price in text file
# Ask what color they want based off of CarType
# Give the different options aswell as the prices for the colors
# Store user answer and the price in text file
# Read back their car decisions and price and ask if they are satisfied with their choice
# If yes then congradulate them on buying an overly expensive car
# If no then ask what they would like to change and re ask the question until satisfied.
# End program

import sys

BuyingCar = False

Opening_Q = 0


TypePrice = 0
CarType = None

ColorPrice = 0
Color = None

TotalPrice = 0





def CarType_Question():
    
    Satisfied_Type = False
    while Satisfied_Type == False:
        CarType = input("""
        You can choose between 3 different car types!
        -Jeep--$10
        -Suv--$15
        -Truck--$5

        Those are your choices now pick one ya stoopid.
        Which one do you want:""").lower()
        if (CarType == "jeep"):
            TypePrice = 10
            Satis = input("""
            You chose a Jeep!
            Are you satisfied with this decision?:""").lower()
            if (Satis == "yes" or Satis == "y"):
                print("Gucci!")
                Satisfied_Type = True
            elif (Satis == "no" or Satis == "n"):
                print("Well then pick the one you want!")
            else:
                print("Invalid response. Please answer 'Yes' or 'No'")
            
    
        elif(CarType == "suv"):
            TypePrice = 15
            Satis = input("""
            You chose as SUV!
            Are you satisfied with this decision?:""").lower()
            if (Satis == "yes" or Satis == "y"):
                print("Gucci!")
                Satisfied_Type = True
            elif (Satis == "no" or Satis == "n"):
                print("Well then pick the one you want!")
            else:
                print("Invalid response. Please answer 'Yes' or 'No'")
            
        elif (CarType == "truck"):
            TypePrice = 5
            Satis = input("""
            You chose a Truck!
            Are you satisfied with this decision?:""").lower()
            if (Satis == "yes" or Satis == "y"):
                print("Gucci!")
                Satisfied_Type = True
            elif (Satis == "no" or Satis == "n"):
                print("Well then pick the one you want!")
            else:
                print("Invalid response. Please answer 'Yes' or 'No'")
        else:
            print("\nPlease select one of the specified types of car.")
    
    return CarType, TypePrice
    


def Color_Question():
    
    Satisfied_Color = False
    colors = ["red", "blue", "white", "black"]
    while Satisfied_Color == False:
        Color = input("""
        Now that you've chosen the type of car you want,
        it's time to pick a color!
        You can Chose between

        -Red--$6
        -Blue--$5
        -White--$2
        -Black--$3
        Those are your choices now pick one ya stoopid
        Which one do you want:""").lower()
        if (Color == colors[0]):
            Check = input("""
            You chose red as your color!
            Are you satisfied with this choice?:""").lower()
            if (Check == "yes" or Check == "y"):
                ColorPrice = 6
                print("Gucci")
                Satisfied_Color = True
            elif (Check == "no" or Check == "n"):
                print("Well then pick one you like!")
            else:
                print("Invalid response. Please answer 'Yes' or 'No'")
                
        elif (Color == colors[1]):
            Check = input("""
            You chose blue as your color!
            Are you satisfied with this choice?:""").lower()
            if (Check == "yes" or Check == "y"):
                ColorPrice = 5
                print("Gucci")
                Satisfied_Color = True
            elif (Check == "no" or Check == "n"):
                print("Well then pick one you like!")
            else:
                print("Invalid response. Please answer 'Yes' or 'No'")
                
        elif (Color == colors[2]):
            Check = input("""
            You chose white as your color!
            Are you satisfied with this choice?:""").lower()
            if (Check == "yes" or Check == "y"):
                ColorPrice = 2
                print("Gucci")
                Satisfied_Color = True
            elif (Check == "no" or Check == "n"):
                print("Well then pick one you like!")
            else:
                print("Invalid response. Please answer 'Yes' or 'No'")
                
        elif (Color == colors[3]):
            Check = input("""
            You chose black as your color!
            Are you satisfied with this choice?:""").lower()
            if (Check == "yes" or Check == "y"):
                ColorPrice = 3
                print("Gucci")
                Satisfied_Color = True
            elif (Check == "no" or Check == "n"):
                print("Well then pick one you like!")
            else:
                print("Invalid response. Please answer 'Yes' or 'No'")
        else:
            print("Please select one of the specified colors")
    return Color, ColorPrice

 

        
def Calculate_Total(TypePrice, ColorPrice, TotalPrice):
    
    TotalPrice = TypePrice + ColorPrice
    return TotalPrice         
    



def Main(CarType, TypePrice, Color, ColorPrice, TotalPrice):
    CarType_Question()
    Color_Question()
    Calculate_Total(TypePrice, ColorPrice, TotalPrice)
    print(CarType_Question(TypePrice))
    
    
    
    
Main(CarType, TypePrice, Color, ColorPrice, TotalPrice)

print(TypePrice)
    



                
                
                















    
    

        


