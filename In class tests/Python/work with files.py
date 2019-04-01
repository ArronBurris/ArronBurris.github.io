#work with files
"""write"""
file = open("text.txt","w")
file.write("Red\n")
file.write("Green\n")
file.write("Blue\n")
file.close()

"""add"""
file = open("text.txt","a")
file.write("Red\n")
file.write("Green\n")
file.write("Grey\n")
file.close()
"""read"""
file = open("text.txt","r")
#print(file.read())
list1 = file.readlines()
print(list1)
file.close()


for line in list1:
    print(line)





file.close()
