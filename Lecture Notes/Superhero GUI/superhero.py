# separate class from main

import random

class Superhero:
    MAX_HEALTHPOINTS = 100  #static since this is the same
    MAX_ATTACKVALUE = 20    # for EVERY superhero object


    def __init__(self, inputName="No name"):
        self.__name = inputName
        self.__healthPoints = Superhero.MAX_HEALTHPOINTS
        self.__attackValue = random.randrange(1, Superhero.MAX_ATTACKVALUE)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getAttackValue(self):
        return self.__attackValue

    def __str__(self):
        tempStr = self.__name
        tempStr += "\nHealth Points: " + str(self.__healthPoints)
        tempStr += "\nAttack Value: " + str(self.__attackValue)
        tempStr += "\n"
        return tempStr

    def getStats(self):
        tempStr = self.__name
        tempStr += "\nHealth Points: " + str(self.__healthPoints)
        tempStr += "\nAttack Value: " + str(self.__attackValue)
        tempStr += "\n"
        return tempStr

    def isAlive(self):
        if self.__healthPoints > 0:
            return True
        else:
            return False

    def loseHealthPoints(self, deductHP):
        self.__healthPoints -= deductHP

    def reset(self):
        self.__healthPoints = Superhero.MAX_HEALTHPOINTS
        self.__attackValue = random.randrange(1, Superhero.MAX_ATTACKVALUE)

