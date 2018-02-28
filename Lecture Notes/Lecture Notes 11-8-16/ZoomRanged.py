from Ranged import Ranged

class ZoomRanged(Ranged):
    def __init__(self, name, damage, zoomLevel):
        super().__init__(name, damage, 5)
        self.__zoomLevel = zoomLevel

    # getters/setters

    def __str__(self):
        msg = super().__str__()
        msg += ", zoom level = " + str(self.__zoomLevel)
        return msg

    def use(self):
        result = self.reduceCapacity(1)
        if result == True:
            print("Zooming...waiting...Fire!")
        else:
            print("Capacity empty")