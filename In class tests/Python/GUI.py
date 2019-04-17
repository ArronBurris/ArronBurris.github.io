#GUI Example

import tkinter as tk


asspuss = tk.Tk()
asspuss.title("I'm gonna shit my pants")
asspuss.geometry("500x500")
asspuss.resizable(0,0)

welcomeLabel = tk.Label(asspuss,text="Eat cum")
welcomeLabel.pack()

countLabel = tk.Label(asspuss, fg="red", text="I'm here")
countLabel.pack()

counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()


counter_label(countLabel)

def exitProgram():
    asspuss.destroy()

exitButton = tk.Button(asspuss, text='Exit', width=25, command=exitProgram)
exitButton.pack()









asspuss.mainloop()
