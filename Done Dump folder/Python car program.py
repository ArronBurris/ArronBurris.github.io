Carprice = 0
Taxpercent = 0.10
Licencepercent = 0.05
Dealerprepcharge = 250
Destinationcharge = 150
Totalcost = 0

Carprice = int(input("How expensive is your car? \nExample: [$9457] \n>"))

Taxadded = Carprice * Taxpercent
Licencefee = Carprice * Licencepercent
Totalcost = Carprice + Taxadded + Licencefee + Dealerprepcharge + Destinationcharge

print("Alright, so your total charge including taxes and the extra preperation \nand transportation fees is <<$" + str(Totalcost) + ">>")
print("Taxes = 10% Car price \nLicence plates = 5% of Car price \nPreperation expenses = $250 \nTransportation expenses = $150")

