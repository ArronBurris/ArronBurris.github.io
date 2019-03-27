#more functions and other shits
#demonstration in functions

EMPTY = " "
NUM_SQUARES = 9


"""
def myFunction(paramaters, go, here = "default"):
    """This is a docstring"""
    print("do stuff")

myFunction2(arguments, go, here) # positional
myFunction(arguments, go) # uses defualt
myFunction(arguments, go, here) #override
myFunction(argumnets = "test", go = "test2", here = "test3") # named

var1 = None
var2 = ""
var3 = 0

var2 = input("enter something")

if var2!="":
    print("do something")

if var1:
    print("Do another thing")
"""
"""
def printBandNames(names):

    print(names[3])
    for name in names:
        print(names)

bandMembers = ["John", "Paul", "George", "Ringo")

printBandNames(bandMembers):
"""
#main
print("here are the instructions")
instructions()

def ask_yes_no(question):
    "Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
print(ask_yes_no("Yes or no?"))

def new_board():
    """Creates a new game boards"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display the game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

gameBoard = new_board()
display_board(gameBoard)
    
