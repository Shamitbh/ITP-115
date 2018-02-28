from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        # label
        self.labelHeader = Label(self,text="Select your toppings.")
        self.labelHeader.grid(row=0, column=2)

        # three check buttons (pizza toppings)

        self.booleanPep = BooleanVar()
        self.booleanSaus = BooleanVar()
        self.booleanCheese = BooleanVar()

        self.checkButton1 = Checkbutton(self,text="Pepperoni", variable=self.booleanPep)
        self.checkButton1.grid(row=1,column=1)

        self.checkButton2 = Checkbutton(self, text="Sausage", variable=self.booleanSaus)
        self.checkButton2.grid(row=1, column=2)

        self.checkButton3 = Checkbutton(self, text="Extra Cheese", variable=self.booleanCheese)
        self.checkButton3.grid(row=1, column=3)

        # three radiobuttons (pizza size)

        self.strvarRadioButton = StringVar()
        self.strvarRadioButton.set("m")

        self.radioButton1 = Radiobutton(self, text="small", value="s", variable=self.strvarRadioButton)
        self.radioButton1.grid(row=2, column=1)

        self.radioButton2 = Radiobutton(self, text="medium", value="m", variable=self.strvarRadioButton)
        self.radioButton2.grid(row=2, column=2)

        self.radioButton3 = Radiobutton(self, text="large", value="l", variable=self.strvarRadioButton)
        self.radioButton3.grid(row=2, column=3)

        # Button for creating an order
        self.buttonOrder = Button(self,text="Create Order", command=self.displayOrder)
        self.buttonOrder.grid(row=3,column=2)


        # Large text field (NOT entry)
        self.text = Text(self, width=50, height=10)
        self.text.grid(row=4,columnspan=4)
        # self.text.configure(state = "disabled")

    def displayOrder(self):
        self.text.configure(state="normal")

        topping = ""
        size = ""

        if self.booleanPep.get() and self.booleanSaus.get() and self.booleanCheese.get():
            # all three toppings
            topping = "pepperoni, sausage, and extra cheese."
        elif self.booleanPep.get() and self.booleanSaus.get():
            # pep and saus
            topping = "pepperoni and sausage."
        elif self.booleanPep.get() and self.booleanCheese.get():
            # pep and cheese
            topping = "pepperoni and extra cheese."
        elif self.booleanSaus.get() and self.booleanCheese.get():
            # saus and cheese
            topping = "sausage and extra cheese."
        elif self.booleanPep.get():
            # pep
            topping = "pepperoni."
        elif self.booleanSaus.get():
            # saus
            topping = "sausage."
        elif self.booleanCheese.get():
            # cheese
            topping = "extra cheese."
        else:
            topping = "no toppings."

        if self.strvarRadioButton.get() == "s":
            size = "small"
        elif self.strvarRadioButton.get() == "m":
            size = "medium"
        else:
            # large
            size = "large"

        self.text.delete(0.0,END)
        self.text.insert(0.0,"Order: One "+size+" pizza with "+topping)
        self.text.configure(state = "disabled")

        # reset all buttons
        self.booleanPep.set(False)
        self.booleanSaus.set(False)
        self.booleanCheese.set(False)
        self.strvarRadioButton.set("m")