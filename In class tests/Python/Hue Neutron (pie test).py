# Calculate discount on the purchase of
# multiple pies

numberOfPies = int(input("Howm many pies would you like to purchase? "))
total = 0

# Calculate Discount
if numberOfPies >= 20:
    total = numberOfPies * 8
elif numberOfPies >= 10:
    total = numberOfPies * 9
elif numberOfPies > 0:
    total = numberOfPies * 10
else:
    print("Please enter a valid number of pies (more than zero")

#print out toal cost
    print ("Total Cost: " + str(total))
