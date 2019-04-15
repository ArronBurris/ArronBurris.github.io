#Exception handling

num = 1

#Lets user know about a problem without erroring our of the program
try:
    print("Number: " + str(num))
except TypeError as e:
    print("types do not match")
    print(e)
except ValueError as e:
    print("some value error")
#Lets user know that it ran correctly
else:
    print("all is well")


try:
    f = open("i_dont_exist","r")
except IOError as e:
    print("the file does not exitst")
    print(e)
