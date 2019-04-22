#Critter

class Critter(object):
    """A Virtual pet"""
    __total = 0  #Double underscore makes value privite to the class it's in

    @staticmethod
    def status():
        print("\nThe total number of critters us: ",Critter.__total)  #defining this into a public fucntion allows __total to be printed but not altered outside of function

    @property
    def name(self):
        return self.__name

    @property
    def mood(self):
        return self.__mood

    @mood.setter
    def mood(self, newMood):
        if (newMood == "Happy" or newMood == "Sad" or newMood == "Grumpy"):
            self.__mood = newMood
            print("successfully updated mood")
        else:
            print("incorrect value for mood")

    def __private_method(self):  #Double underscore can be applied to any value or function
        print("This is a private method")

    def public_method(self):
        print("This is the public method")
        self.__private_method()

    def __init__(self, name, mood):
        print("A shit is alive")
        self.__name = name
        self.__mood = mood
        Critter.__total += 1

    def talk(self):
        print("Hi! I'm a shit")


critter1 = Critter("Stain", "Depressed") #self in first def is "critter1"
critter1.talk()
print(critter1.name)

print(critter1.name)

Critter.status
critter1.public_method()

print(critter1.mood)
critter1.mood = "Angry"
print(critter1.mood)
critter1.mood = "Grumpy"
print(critter1.mood)
critter1.mood = "shit"
print(critter1.mood)
