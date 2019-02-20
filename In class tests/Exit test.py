#loop test
#userExit = "no"

#whie(userExit == "no" or userExit == "n"):
#   print("Hi")
#   userExit = (input("Do you want to exit?")).lower()


userExit = "no"

while(userExit == "no" or userExit == "n"):
    print("Hi")
    userExit = (input("Do you want to exit?")).lower()


userInput = int(input("how many cars do you want to buy?"))

while (userInput < 1 or userInput > 15):
    userInput = int(input("How many cars do you want to buy? \nAt least 15 or more than 1 car."))
