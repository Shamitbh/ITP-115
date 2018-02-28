from Being import Being

class Vampire(Being):
    MAX_BLOOD = 5
    HUNGER_LEVELS = ["starving", "hangry", "hungry", "content", "full", "stuffed"]

    def __init__(self, name, quarts, animal):

        # call parent constructor
        super().__init__(name, quarts)

        # set up new attribute representing Vampire's animal form
        self.__mAnimalForm = animal

    def getAnimal(self):
        return self.__mAnimalForm

    def setAnimal(self, animal):
        self.__mAnimalForm = animal

    def getHunger(self):
        return Vampire.HUNGER_LEVELS[self.getQuarts()]

    def isStuffed(self):
        if self.getQuarts() == Vampire.MAX_BLOOD:
            return True
        else:
            return False

    def suckBlood(self, humanObj):
        humanObj.decreaseQuarts()
        self.increaseQuarts()

    def __str__(self):
        msg = self.getName() + " is " + self.getHunger()
        return msg