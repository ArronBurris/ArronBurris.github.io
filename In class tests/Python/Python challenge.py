import random
print("Wanna play a game? A game of coin tossing?")
print("I'm gonna flip a coin 100 times and you guess which side it will land on more often.")

Heads = 0
Tails = 0
Tosses = 0

while Tosses < 100:
    coin = random.randrange(2)
    if coin == 0:
         Heads = Heads + 1
    else:
        Tails = Tails + 1
    Tosses = Tosses + 1

print("Heads-" + str(Heads))
print("Tails-" + str(Tails))
    
    
    
