#Python Final Project

# Ask if they want to buy a car
# Ask what kind of car they want
# Give the different options aswell as the prices for them
# Store user answer and the price in text file
# Ask what color they want based off of cartype
# Give the different options aswell as the prices for the colors
# Store user answer and the price in text file
# Read back their car decisions and price and ask if they are satisfied with their choice
# If yes then congradulate them on buying an overly expensive car
# If no then ask what they would like to change and re ask the question until satisfied.
# End program


import tkinter as tk

box = tk.Tk()
box.title("Final Project")
box.geometry("500x500")
box.resizable(0,0)

welcomelabel = tk.Label(box, text="Welcome to this shitty GUI")
welcomelabel.pack()

class GUI:

    def __init__(self):
        


