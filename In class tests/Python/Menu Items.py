#menu items

menuItems = []
userExit = False

while(userExit == False):
    item = input("Please enter an item to add to the menu: ")
    menuItems.append(item)
    userExit = input("Do you want to add aditional items tothe menu? ")
    if (userExit == "no" or userExit == "n"):
        userExit = True 

print(menuItems)
