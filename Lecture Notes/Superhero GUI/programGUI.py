#initially one file--
# separate class from main

from tkinter import *
from application import Application


def main():
    root = Tk()
    root.title("Superhero")
    root.geometry("600x400")

    app = Application(root)
    root.mainloop()
main()