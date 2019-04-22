# Black Jack

import Cards

card1 = Cards.Card("A", "S", True)

print(card1)

card2 = Cards.Card("9", "C", True)

print(card2)

deck1 = Cards.Deck()
deck1.populate()
print(deck1)
deck1.shuffle()
print(deck1)
player_hand1 = Cards.Hand()
player_hand2 = Cards.Hand()

deck1.deal([player_hand1, player_hand2],5)
