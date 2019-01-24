pricePerSong = .99
numberOfSongs = 0
totalPrice = 0

numberOfSongs = int(input("How many songs?"))
totalPrice = numberOfSongs * pricePerSong
if numberOfSongs >= 10:
    totalPrice = totalPrice - 1
else:
    totalPrice = totalPrice + 0
if numberOfSongs >= 10:
    print ("Total price: $" + str (totalPrice))
    print ("YOU GOT A $1 DISCOUNT FOR BUYING 10 OR MORE SONGS!!")
    print ("Congratulation! Now have a Parrot")
    print ("                                .---.")
    print ("                               .'  .-.'._")
    print ("                             _/   (  0 / ',")
    print ("                          .-' \   (   /--./")
    print ("                        .'.  ' |'.__.'--'")
    print ("                       / '-/_, |'  |")
    print ("                      / /_.   ;    ;")
    print ("                     /_.' , '/    /")
    print ("___________________ /_`-'_-' _.-'__________________")
    print ("__________________________\\\_\\\____________________")
    print ("                   |_/,/ .|`` ``")
    print ("                   / \_/-/")
    print ("                   |`| ; |")
    print ("                   \/' \ /")
    print ("                    |'.|`")
    print ("                     \_/")
else:
    print("Total price: $" + str(totalPrice))
    print("Act now and you can get $1 off buy purchasing 10 or more songs!!")

totalPrice = str(totalPrice)
