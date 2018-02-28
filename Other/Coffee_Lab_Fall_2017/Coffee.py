
class Coffee(object):
    statuses = ["ordered", "completed"]
    def __init__(self, size, desc, customer):
        self.__size = size
        self.__desc = desc
        self.__customer = customer
        self.__status = 0

    def setCompleted(self):
        self.__status = 1

    def __str__(self):
        msg = self.__size
        msg += " " + self.__desc
        msg += " for " + self.__customer
        msg += " (" + Coffee.statuses[self.__status] + ")"

        return msg