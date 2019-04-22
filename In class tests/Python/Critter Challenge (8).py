#Critter Challenge
"""
class Critter(object):
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name
        total = 0

    @staticmethod
    def status():
        print("\nThe total number of critters is", Critter.total)

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Hi. I'm", self.name, "\n")

crit1 = Critter("Coochie")
crit1.talk()

crit2 = Critter("Randal")
crit2.talk()

print("Directly accessing crit1.name")
print(crit1.name)

input("\n\Press the enter eky to exit")


crit = Critter()

crit.talk()

input("*\n\Press the enter key to exit.")"""

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time

    def eat(self, hungerReduce = 4, food = 0):
        food = input("Please feed me master. How many apples will you allow me to have?")
        hungerReduce == hungerReduce * food
        print("Brruppp. Nya, thank you so much master!")
        self.hunger -= hungerReduce
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, boredomReduce = 0, fun = 0):
        fun = input("Yay, fun times with master! How many minutes are we gonna play for?")
        boredomReduce == boredomReduce * fun
        print("Yay!", self.name, "had so much fun with master!", self.name, "wishes to play again soon!")
        self.boredom -= boredomReduce
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("what do you want to name your critter?: ")
    print\
    ("""
    DISCLAIMER!

    The text I used for the inputs in this assignment are meant to
    make you feel uncomfortable when you run it. KEK
    """)
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
                    
        # feed your critter
        elif choice == "2":
            crit.eat()

        # play with your critter
        elif choice == "3":
            crit.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isnt' a valid choice.")

main()
("\n\nPress the enter key to exit.")
                      
            
            
            
                
        
        

    













































