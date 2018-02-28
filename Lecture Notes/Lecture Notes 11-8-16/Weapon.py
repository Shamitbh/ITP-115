# Use inheritance (video game and need weapons from a class)

'''

First think about attributes shared by every weapon:
-Damage dealt
-Name
-energy to use? (hard to implement)
-accuracy (hard to implement)

Methods:
-init
-str
-get/set
-use()

'''

class Weapon(object):

    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    # Getters
    def getName(self):
        return self.__name

    def getDamage(self):
        return self.__damage

    # Setters
    def setName(self, name):
        self.__name = name

    def setDamage(self, damage):
        self.__damage = damage

    def __str__(self):
        msg = self.__name + ", damage value = " + str(self.__damage)
        return msg

    def use(self):
        print("Using generic weapon")