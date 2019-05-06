# text adventure

Num_Rooms = 9

Num_Walls = 4

EMPTY = """   """

Door = False

class Rooms(object):

    def Grid():
        Grid = []
        for room in range(Num_Rooms):
            Grid.append(EMPTY)
        return Grid

    def Display_Grid(Grid):
        print("   A   B   C  ")
        print(" -------------")
        print("1" + "|" + Grid[0] + "|" + Grid[1] + "|" + Grid[2] + "|")
        print(" -------------")
        print("2" + "|" + Grid[3] + "|" + Grid[4] + "|" + Grid[5] + "|")
        print(" -------------")
        print("3" + "|" + Grid[6] + "|" + Grid[7] + "|" + Grid[8] + "|")
        print(" -------------")

class Movement():
    
        
   
            
"""
    def Room():

    def Walls():

    def Door():
        Locked = False
        if Locked = True:
            Move = False"""

def main():
    NewGrid = Rooms.Grid()
    print("This is the Deku Tree Grid")
    Rooms.Display_Grid(NewGrid)
    

main()
