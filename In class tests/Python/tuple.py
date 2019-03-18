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

score = {"moe":[1000, "springfield", "north"],"curley":[1200, "springfield", "north"],"lary":[1500, "springfield", "north"]}
print(score["curley"])

for key,value in score.items():
    print(key,value[0],value[1])
