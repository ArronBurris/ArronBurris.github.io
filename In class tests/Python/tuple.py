#arrays

#tuple
"""
import random
colors = ("red", "green", "blue")

print(colors[random.randint(0,2)])

for color in colors:
    print(color)
"""

#list
"""
colors = ["red", "green", "blue"]

colors[2] = "gray"

print(colors)
"""

#nested list
"""
scores = [[("moe",1000),("curley",1200),("larry",1500)]]

print(scores[0][1])
scores[0][1] = 1300
print(scores)
"""

#dictionary
"""
score = {"moe":[1000, "springfield", "north"],"curley":[1200, "springfield", "north"],"lary":[1500, "springfield", "north"]}
print(score["curley"])

for key,value in score.items():
    print(key,value[0],value[1])

def function1():
    var1 = input("Write something: ")
    var2 = input("Write something: ")
    var3 = input("Write something: ")
    return var1, var2, var3

def function2(var1, var2, var3):
    print(var1)
    print(var2)
    print(var3)

var1, var2, var3 = function1()
function2(var1, var2, var3)"""

shit = 0

def hell(shit):
     shit = 2 
     return shit
    


def second(shit):
    hell(shit)
    print (hell(shit))

second(shit)

    
