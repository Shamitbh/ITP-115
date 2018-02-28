from Weapon import Weapon

'''
Ranged class will get name and damage from weapon

What new attributes should we add to range class?
-Distance
-Velocity
-height?
-   Capacity (how many fireballs does mario get to throw?)
-Fire rate

'''

class Ranged(Weapon):
    def __init__(self, name, damage, capacity):

        # must always call the parent constructor using Super
        super().__init__(name, damage)

        # set up our NEW attribute
        self.__capacity = capacity

    def getCapacity(self):
        return self.__capacity


    # Subtract num from current capacity - sort of like a setCapacity
    def reduceCapacity(self, num):
        if self.__capacity - num >= 0:
            self.__capacity -= num
            return True
        else:
            return False

    # if we DONT define use, we inherit it from weapon
    # BUT we can override (aka re-define) if we want
    def use(self):
        result = self.reduceCapacity(1)
        if result == True:
            # we successfully fired our weapon
            print("Firing " + self.getName() + " (Capacity = " + str(self.__capacity) + ")")
        else:
            print("Out of capacity")

    def __str__(self):
        # call parent version
        msg = super().__str__()
        msg += ", capacity = " + str(self.__capacity)
        return msg