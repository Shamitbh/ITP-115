from Being import Being

class Human(Being):

    def __init__(self, name, quarts, bloodType):

        # call parent constructor
        super().__init__(name, quarts)

        # set up new attribute representing human's blood type
        self.__mBloodType = bloodType

    def getBloodType(self):
        return self._mBloodType

    def setBloodType(self, bloodType):
        self.__mBloodType = bloodType

    def isAlive(self):
        if self.getQuarts() > 0:
            return True
        else:
            return False

    def __str__(self):
        msg = "Human " + super().getName() + " has " + str(super().getQuarts()) + " quarts of type "
        msg += str(self.__mBloodType) + " blood."
        return msg