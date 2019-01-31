pricePerSong = .99
numberOfSongs = 0
totalPrice = 0

numberOfSongs = int(input("How many songs?"))
totalPrice = numberOfSongs * pricePerSong
if numberOfSongs >= 10: totalPrice = totalPrice - 1
else: totalPrice = totalPrice + 0
print("Total price: $" + str(totalPrice))
totalPrice = str(totalPrice)
