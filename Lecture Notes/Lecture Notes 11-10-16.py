from tkinter import *
# THIS IS INTRO TO GUI (graphical user interface)

# create a custom frame class that inherits from frame
class Application(Frame):
    def __init__(self, rootWindow):
        # Always call parent constructor
        super().__init__(rootWindow)

        # Since this class IS a FRAME, we can call GRID to make it appear
        self.grid()

        self.ent1 = Entry(self)
        self.ent1.grid()

        self.ent2 = Entry(self)
        self.ent2.grid(row=0,column=2)

        # DONT PUT PARETNHESES AFTER ACTIONDOUBLE BECAUSE YOU ONLY WANT IT TO HAPPEN WHEN USER CLICKS
        self.buttonDouble = Button(self, text="Double", font="Arial 16", command=self.actionDouble)
        self.buttonDouble.grid(row = 0,column=1, rowspan=2)

        self.buttonLowercase = Button(self, text="Lowercase", font="Arial 16", command=self.actionLowercase)
        self.buttonLowercase.grid(row=2,column=1)

        self.labelInfo = Label(self,text="Some awesome msg",font="Arial 16")
        self.labelInfo.grid(row=1,column=0)



        # special string variable to store what radio button is selected
        # have one of these for each group of radio buttons
        self.strvarCreditCard = StringVar()
        self.strvarCreditCard.set("v")



        self.radioMasterCard = Radiobutton(self, text="I am paying for this bike with a Master Card", value="mc",
                                           font="Arial 16", variable=self.strvarCreditCard)
        self.radioMasterCard.grid(row=3,column=0)

        self.radioVisa = Radiobutton(self, text="I am paying for this bike with a Visa", value="v",
                                           font="Arial 16", variable=self.strvarCreditCard)
        self.radioVisa.grid(row=4, column=0)

        #  -----------------------

        # create special boolean variable to store whether checkbox checked or not
        self.booleanTerms = BooleanVar()
        #self.booleanTerms.set(False)

        self.checkTerms = Checkbutton(self, text="Accept terms and conditions?", font="Arial 16", variable=self.booleanTerms)
        self.checkTerms.grid(row = 5, column = 0)




    def actionDouble(self):
        # get the text from ent1, and write it TWICE into ent2
        msg = self.ent1.get()
        self.ent2.delete(0,END)
        self.ent2.insert(0,msg+msg)

    def actionLowercase(self):
        self.ent2.delete(0, END)
        self.ent2.insert(0, self.strvarCreditCard.get())

        if self.booleanTerms.get() == True: # button is checked
            self.ent1.delete(0,END)
            self.ent1.insert(0,"Thanks for accepting our terms/conditions")
        else:
            self.ent1.delete(0,END)
            self.ent1.insert(0, "You made the right choice")

        # msg = self.ent1.get()
        # self.ent2.delete(0,END)
        # self.ent2.insert(0, msg.lower())


        # # Create a button and label it with text
        # self.buttonClickMe = Button(self, text="Hey a button!", fg="#F2700B")
        # self.buttonClickMe.grid()
        #
        # # Create a label
        # self.labelCollege = Label(self, text="University of Southern California\nFight On!", fg="yellow", bg="red",
        #                      font="Ariel 20 underline")
        # self.labelCollege.grid()
        #
        # # Create an entry
        # self.entryName = Entry(self)
        # self.entryName.grid()


def main():
    # create a main window
    root = Tk()

    # set parameters (height/width)
    root.geometry("500x500")

    # Set title
    root.title("Our first GUI!")

    windowApp = Application(root)

    # when you call main loop, any code after will not execute
    # until after main loop is closed
    root.mainloop()


main()