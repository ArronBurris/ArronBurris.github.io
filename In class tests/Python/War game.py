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

deck = {"heart1":1, "heart2":2, "spade1":1, "spade2":1}
