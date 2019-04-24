#War Game

#each card has a suite and number
#make only 4 of each card
#each player picks random card
#highest card winds
#tie braker - 3 cards face down, 1 up , winnder takes all
#52
#Winner is determined by who has all cards at the end

#build and shuffle the deck
#create players
#deal cards
#play the game

import Cards
import math

class War_Card(Cards.Card):
    """A War Card, Aces High"""
    @property
    def value(self):
        if self.is_face_up:
            if self.rank == "J":
                v = 11
            elif self.rank == "Q":
                v = 12
            elif self.rank == "K":
                v = 13
            elif self.rank == "A":
                v = 14
            else:
                v = War_Card.RANKS.index(self.rank) + 1
        else:
            v = None
        return v

class War_Deck(Cards.Deck):
    """A War Deck"""
    def populate(self):
        for suit in War_Card:
            for rank in War_Card>RANKS:
                self.add(War_Card(rank.suit))
"""
card1 = War_Card("A", "s")
print(card1)
print(card1.value)

card2 = War_Card("A", "c")
print(card2)
print(card2.value)"""


deck = War_Deck()
print(deck)
deck.populate()
print(deck)

"""
def create_players(numberOfPlayers = 2):
    players = []
    for person in range (numberOfPlayers):
        players.append("Player" + str(person))
    return players

def build_deck():
    deck = {}
    suites = ["Hearts","Clubs","Diamonds","Spades"]
    for suite in suites:
        for number in range(13):
            deck[suite + str(number + 1)] = number + 1
    return deck

def deal(deck,players):

players = create_players()
print(players)
deck = build_deck()
print(deck)




suites = {"hearts": [1,2,3,4,5], "spades":[1,2,3,4,5]}

deck = {"heart1":1, "heart2":2, "spade1":1, "spade2":1}"""
