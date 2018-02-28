
class Being(object):

    def __init__(self, name, quarts):
        self.__mName = name
        self.__mQuarts = quarts

    # Getter methods
    def getName(self):
        return self.__mName

    def getQuarts(self):
        return self.__mQuarts

    # Setter methods
    def setName(self, name):
        self.__mName = name

    def setQuarts(self, quarts):
        self.__mQuarts = quarts

    def increaseQuarts(self):
        self.__mQuarts += 1

    def decreaseQuarts(self):
        self.__mQuarts -= 1
