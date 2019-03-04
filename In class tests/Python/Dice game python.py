#dice game
import random
UserGuess = 0
UserGuessAgain = "yes"
die1 = 0
die2 = 0


print("Welcome to the OTC CIS 120 Casino!")


while (UserGuess == 0 or (UserGuess < 2 or UserGuess > 12)):
    try:
        UserGuess = int(input("Please enter a number between 2 and 12 "))
    except:
        print("Fuck you and your invalid number, enter something between 2 and 12 bitch!")
        continue
    

print("You guessed " + str(UserGuess))

while(UserGuessAgain == "yes" or UserGuessAgain == "y"):
    while (UserGuess == 0 or (UserGuess < 2 or UserGuess > 12)):
        try:
            UserGuess = int(input("Please enter a number between 2 and 12 "))
        except:
            print("Fuck you and your invalid number, enter something between 2 and 12 bitch!")
            continue


    while  (UserGuess > 1 and UserGuess < 13):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print("Die1: " + str(die1))
        print("Die2: " + str(die2)) 
        #break

        if(UserGuess == die1 + die2):
            print("You fuckin did the thing you saucey bitch")
        else:
            print("You fucked up you little whore")

        

        #break

        UserGuessAgain = input("Do you want to play again?")
        while (UserGuessAgain != "yes" and UserGuessAgain != "y" and UserGuessAgain != "no" and UserGuessAgain != "n"):
                UserGuessAgain = input("Please enter yes(y) or no(n)?")

        UserGuess = 0

