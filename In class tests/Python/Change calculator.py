#declar variables
numQuarters = 0
numDimes = 0
numNickels = 0
numPennies = 0
amountOfChange = 0

amountOfChange = int(input("How much change do you want?"))

while(amountOfChange > 0):

    if (amountOfChange >=25):
        numQuarters = numQuarters + 1
        amountOfChange = amountOfChange - 25
    elif (amountOfChange >= 10):
        numDimes = numDimes + 1
        amountOfChange = amountOfChange - 10
    elif (amountOfChange >= 5):
        numNickels = numNickels + 1
        amountOfChange = amountOfChange - 5
    elif (amountOfChange >= 1):
        numPennies = numPennies + 1
        amountOfChange = amountOfChange - 1
"""

while(amountOfChange >= 25):
    numQuarters = numQuarters + 1
    amountOfChange = amountOfChange - 25

while(amountOfChange >= 10):
    numDimes = numDimes + 1
    amountOfChange = amountOfChange - 10

while(amountOfChange >= 5):
    numNickels = numNickels + 1
    amountOfChange = amountOfChange - 5

while(amountOfChange >= 1):
    numPennies = numPennies + 1
    amountOfChange = amountOfChange - 1
"""

#end while
print("Your change:")
print("Quarters: " + str(numQuarters))
print("Dimes: " + str(numDimes))
print("Nickels: " + str(numNickels))
print("Pennies: " + str(numPennies))

while(True):
    userInput = input("do you want to exit?")
    if (userInput == "yes"):
        break
