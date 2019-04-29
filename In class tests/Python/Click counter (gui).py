# Click Counter

from tkinter import *

class Application(Frame):
    # Gui Application that counts button clicks
    def __init__(self, master):
        #initialize the fram
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        # Create button wich desplays number of clicks
        self.bttn = Button(self)
        self.bttn["text"] = "Total clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        # increase click count
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)


root = Tk()
root.title("Click Counter")
root.geometry("200x200")

app = Application(root)

root.mainloop()
