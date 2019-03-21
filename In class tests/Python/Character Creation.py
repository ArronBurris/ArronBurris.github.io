
#Character creation


print("you have 30 points to divide up between 4 attributes... have fun.")
Add = 0
Sub = 0 
Strength = 0
Dexterity = 0
Wisdom = 0
Health = 0
Points = 30
Change = False

print("You can chose between Strength, Wisdom, Dexterity, and Health")

while (Points > 0):
    
      
    WhichOne = str(input("Type out the one you wish to edit."))  
    if (WhichOne == "Strength" or WhichOne =="strength" or WhichOne == "Str" or WhichOne == "str"):
        AddorSub = str(input("Do you want to add or subtract?"))
        if (AddorSub == "Add" or AddorSub == "add"):  
            Add = int(input("How much for strength?"))
            if (Add <= Points):
                Strength = Strength + Add
            if (Add > Points):
                print("Please alocate an amount that is equal to or less than " + str(Points))
            elif (Strength <= Points):
                Points = Points - Add
                print("Strength = " + str(Strength))
                print("Dexterity = " + str(Dexterity))
                print("Wisdom = " + str(Wisdom))
                print("Health = " + str(Health))
                print("Points left = " + str(Points))
            if (Points == 0):
                break
        elif (AddorSub == "Subtract" or AddorSub == "subtract"):
            if (Strength == 0):
                print("Don't be dumb please")
            elif (Strength > 0 and Strength <= 30):
                Sub =  int(input("How much to take away from  "))
                if (Sub > Points):
                    print("Please alocate an amount that is equal to or less than " + str(Points))
                elif (Sub <= Points):
                    Points = Points + Sub
                    Strength = Strength - Sub
                    print("Strength = " + str(Strength))
                    print("Dexterity = " + str(Dexterity))
                    print("Wisdom = " + str(Wisdom))
                    print("Health = " + str(Health))
                    print("Points left = " + str(Points))
                    

                        
    elif (WhichOne == "Dexterity" or WhichOne == "dexterity" or WhichOne == "Dex" or WhichOne == "dex"):
        AddorSub = str(input("Do you want to add or subtract?"))
        if (AddorSub == "Add" or AddorSub == "add"):
            Add = int(input("How much for Dexterity?"))
            if (Add <= Points):
                Dexterity = Dexterity + Add
            if (Add > Points):
                print("Please alocate an amount that is equal to or less than " + str(Points))
            elif (Dexterity <= Points):
                Points = Points - Add
                print("Strength = " + str(Strength))
                print("Dexterity = " + str(Dexterity))
                print("Wisdom = " + str(Wisdom))
                print("Health = " + str(Health))
                print("Points left = " + str(Points))
            if (Points == 0):
                break
        elif (AddorSub == "Subtract" or AddorSub == "subtract"):
            if (Dexterity == 0):
                print("Don't be dumb please")
            elif (Dexterity > 0 and Dexterity <= 30):
                Sub =  int(input("How much to take away from  "))
                if (Sub > Points):
                    print("Please alocate an amount that is equal to or less than " + str(Points))
                elif (Sub <= Points):
                    Points = Points + Sub
                    Dexterity = Dexterity - Sub
                    print("Strength = " + str(Strength))
                    print("Dexterity = " + str(Dexterity))
                    print("Wisdom = " + str(Wisdom))
                    print("Health = " + str(Health))
                    print("Points left = " + str(Points))


                    
    elif(WhichOne == "Wisdom" or WhichOne == "wisdom" or WhichOne == "Wis" or WhichOne == "wis"):
        AddorSub = str(input("Do you want to add or subtract?"))
        if (AddorSub == "Add" or AddorSub == "add"):  
            Add = int(input("How much for Wisdom?"))
            if (Add <= Points):
                Wisdom = Wisdom + Add
            if (Add > Points):
                print("Please alocate an amount that is equal to or less than " + str(Points))
            elif (Wisdom <= Points):
                Points = Points - Add
                print("Strength = " + str(Strength))
                print("Dexterity = " + str(Dexterity))
                print("Wisdom = " + str(Wisdom))
                print("Health = " + str(Health))
                print("Points left = " + str(Points))
            if (Points == 0):
                break
        elif (AddorSub == "Subtract" or AddorSub == "subtract"):
            if (Wisdom == 0):
                print("Don't be dumb please")
            elif (Wisdom > 0 and Wisdom <= 30):
                Sub =  int(input("How much to take away from  "))
                if (Sub > Points):
                    print("Please alocate an amount that is equal to or less than " + str(Points))
                elif (Sub <= Points):
                    Points = Points + Sub
                    Wisdom = Wisdom - Sub
                    print("Strength = " + str(Strength))
                    print("Dexterity = " + str(Dexterity))
                    print("Wisdom = " + str(Wisdom))
                    print("Health = " + str(Health))
                    print("Points left = " + str(Points))
        
    elif(WhichOne == "Health" or WhichOne == "health" or WhichOne == "HP" or WhichOne == "Hp" or WhichOne == "hp"):
        AddorSub = str(input("Do you want to add or subtract?"))
        if (AddorSub == "Add" or AddorSub == "add"):      
            Add = int(input("How much for Health?"))
            if (Add <= Points):
                Health = Health + Add
            if (Add > Points):
                print("Please alocate an amount that is equal to or less than " + str(Points))
            elif (Health <= Points):
                Points = Points - Add
                print("Strength = " + str(Strength))
                print("Dexterity = " + str(Dexterity))
                print("Wisdom = " + str(Wisdom))
                print("Health = " + str(Health))
                print("Points left = " + str(Points))
            if (Points == 0):
                break
        elif (AddorSub == "Subtract" or AddorSub == "subtract"):
            if (Health == 0):
                print("Don't be dumb please")
            elif (Health > 0 and Health <= 30):
                Sub =  int(input("How much to take away from  "))
                if (Sub > Points):
                    print("Please alocate an amount that is equal to or less than " + str(Points))
                elif (Sub <= Points):
                    Points = Points + Sub
                    Health = Health - Sub
                    print("Strength = " + str(Strength))
                    print("Dexterity = " + str(Dexterity))
                    print("Wisdom = " + str(Wisdom))
                    print("Health = " + str(Health))
                    print("Points left = " + str(Points))
if (Points == 0):
    Ask = str(input("Are you happy with your stats?"))
    if (Ask == "Yes" or Ask == "yes" or Ask == "Y" or Ask == "y"):
        print("Well then go on and kill some things with you new abilities!")
    elif (Ask == "No" or Ask == "no" or Ask == "N" or Ask == "n"):
        print("Well too bad, you can't re-roll in my DnD games, cus my mom is making pizza for us so what I say goes.")


                       
        








