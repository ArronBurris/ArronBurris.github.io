#reference vs value
"""
name = "Bill"

name = name.upper()

print(name.upper())

print(name*3) 
"""
#sorting

arrayA = [2, 3, 1]

print(sorted(arrayA))

print(arrayA)

arrayA.sort()

print(arrayA)


#tuples

arrayB = ("blue","white","red")

print(sorted(arrayB))

#arrayB.sort()

arrayC = {1:"john",2:"paul",3:"george",4:"ringo"}

print(sorted(arrayC,reverse=True))

if (arrayB.index("white")):
          print("found!")

if (arrayA.index(2)):
    print("found 2!")


if "white" in arrayB:
    print("phound 3!")



for color in arrayB:
    if color == "white":
        print("found 4")
        break
