# Shamit Bhatia
# ITP 115, Fall 2016
# Assignment 9
# Shamitbh@usc.edu
# Purpose: Create a Superhero class and use other classes.

class Superhero(object):

    def __init__(self, name, type, attack):
        self.__name = name
        self.__type = type
        self.__attack = int(attack)
        self.__health = 100

    def getName(self):
        return self.__name.title()

    def getAttack(self):
        return self.__attack

    def getHealth(self):
        return self.__health

    def getType(self):
        return self.__type

    def loseHealth(self, attack):
        self.__health -= attack

    def isDead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def __str__(self):
        msg = self.__name.title() + " the " + self.__type.lower() + " has " + str(self.__attack)
        msg += " attack points and currently has " + str(self.__health) + " points of health."
        return msg
