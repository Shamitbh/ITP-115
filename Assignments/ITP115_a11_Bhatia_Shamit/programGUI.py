from tkinter import *
from pizzaGUI import Application


def main():
    root = Tk()
    root.title("Pizza Order")
    root.geometry("362x258")
    root.configure(background = 'grey')

    app = Application(root)

    root.mainloop()

main()