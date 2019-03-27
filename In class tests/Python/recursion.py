#recursion
"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
"""

#functions

import math
userExit = False

def squareshit(side):
    area = side * side
    return area

def circleshit(rad):
    area = 3.14 * (rad * rad)
    return area

def triangleshit(side):
    area = (math.sqrt(3)/4) * (side * side)
    return area

while(True):
    print("Do you want to calculate:")
    print("1.Area of a square")
    print("2.Area of a circle")
    print("3.Area of a triangle")
    print("0.Exit")
    userChoice = input("Enter Choice:")
    
    if userChoice == "1":
        side = int(input("How long is one side of the square?"))
        print("The area is " + str(squareshit(side)))

    elif userChoice == "2":
        rad = int(input("How long is the radius of the circle?"))
        print("The area is " + str(circleshit(rad)))

    elif userChoice == "3":
        side = int(input("How long is the radius of the circle?"))
        print("The area is " + str(triangleshit(side)))

    elif userChoice == "0":
        False 
        
              
"""          
print(squareshit(3))
print(circleshit(5))
print(triangleshit(9))
"""
