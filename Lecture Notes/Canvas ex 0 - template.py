
from tkinter import *


class Application(Frame):
    def __init__(self, root):
        #call PARENT constructor, AKA FRAME
        super().__init__(root)
        #Application inherits from Frame
        #Frame needs to call grid() to appear on the screen
        #therefore, Application also has to call grid
        self.grid()

        self.canvas = Canvas(self, width=1000, height=700, bg="black")
        self.canvas.grid()

        self.greenOval = self.canvas.create_oval(700, 500, 900, 600, fill="green")
        self.whiteSquare = self.canvas.create_rectangle(50, 600, 100, 650, fill="white")

        # this means: whenever ANY key, the keypress method will be triggered
        self.canvas.bind("<Key>", self.keyPress)
        self.canvas.focus_set()

        # canvas.move(shapeId, changeX, changeY)
        self.gameLoop()

    def keyPress(self, event):
        if event.keysym == "Up":
            self.canvas.move(self.whiteSquare, 0, -20)
        elif event.keysym == "Down":
            self.canvas.move(self.whiteSquare, 0, 20)
        elif event.keysym == "Right":
            self.canvas.move(self.whiteSquare, 20, 0)
        elif event.keysym == "Left":
            self.canvas.move(self.whiteSquare, -20, 0)
        self.canvas.update()

    def gameLoop(self):
        # self.canvas.move(self.whiteSquare, 10, 0)

        # this will give us the topright (xy) and bottom left (xy)
        coords = self.canvas.coords(self.whiteSquare)
        if coords[2] >= 1050:
            self.canvas.move(self.whiteSquare, -1050, 0)


        # after is a function that calls another function after certain delay of x milliseconds
        # always call after at the end
        self.after(10, self.gameLoop)


def main():
    #create our main window
    root = Tk()
    root.title("Game_Example")
    root.geometry("1000x700")
    app = Application(root)

    root.mainloop()

main()