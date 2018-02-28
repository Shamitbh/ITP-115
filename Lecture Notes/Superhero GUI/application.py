from tkinter import *
from superhero import Superhero

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        self.buttonStart = Button(self, text="Start Game", command=self.startGame)
        self.buttonStart.grid(row=0,column=1)

        self.entName1 = Entry(self)
        self.entName1.grid(row=1,column=0)
        self.labelPrompt = Label(self,text="Enter player names")
        self.labelPrompt.grid(row=1,column=1)
        self.entName2 = Entry(self)
        self.entName2.grid(row=1,column=2)


        self.textStats1 = Text(self, width=20,height=20)
        self.textStats1.grid(row=2,column=0)

        self.labelStats = Label(self,text="Hero Stats")
        self.labelStats.grid(row=2,column=1)

        self.textStats2 = Text(self, width=20, height=20)
        self.textStats2.grid(row=2, column=2)

        self.buttonFight = Button(self,text="Fight!",command=self.fight)
        self.buttonFight.grid(row=3,column=1)

        # create a superhero object and store in frame. Cannot store in main with GUI
        self.p1 = Superhero()
        self.p2 = Superhero()

    def startGame(self):
        # assign the neames the player has typed to superhero
        name1 = self.entName1.get()
        name2 = self.entName2.get()

        if name1 == "":
            name1 = "Wonder Woman"
        if name2 == "":
            name2 = "Batman"

        self.p1.setName(name1)
        self.p2.setName(name2)

    def fight(self):
        #show initial stats
        self.textStats1.insert(0.0,self.p1.getStats())
        self.textStats2.insert(0.0,self.p2.getStats())

        while self.p1.isAlive() and self.p2.isAlive():
            self.p1.loseHealthPoints(self.p2.getAttackValue())
            self.p2.loseHealthPoints(self.p1.getAttackValue())

        self.textStats1.insert(0.0, self.p1.getStats())
        self.textStats2.insert(0.0, self.p2.getStats())