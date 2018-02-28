
from Coffee import Coffee

class Barista(object):
    maxOrders = 5

    def __init__(self, name):
        self.__name = name
        self.__orders = []

    def takeOrder(self):
        drink = input("What drink do you want? ")
        size = input("What size do you want? ")
        name = input("Whats your name? ")
        myCoffee = Coffee(size, drink, name)
        self.__orders.append(myCoffee)
        print(myCoffee)
    def isAcceptingOrders(self):
        if len(self.__orders) < Barista.maxOrders:
            return True
        else:
            return False

    def makeDrinks(self):
        print("Here are the orders: ")
        for coffee in self.__orders:
            coffee.setCompleted()
            print(coffee)
        self.__orders = []

    def __str__(self):
        msg = self.__name
        return msg