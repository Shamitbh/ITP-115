
class Shape(object):
    numOfShapes = 0;

    def __init__(self, name):
        self.__name = name


    # get or acessor method
    def getName(self):
        return self.__name


    # set or mutator method
    def setName(self, name):
        self.__name = name

    def __str__(self):
        msg = "Name: " + self.__name
        return msg

    def calcArea(self):
        return 0


class Rectangle(Shape):

    # constructor method
    def __init__(self, name, width, height):
        super().__init__(name)
        self.__width = width
        self.__height = height

    def __str__(self):
        msg = "Width " + str(self.__width)
        msg += " Height: "+ str(self.__height)
        return super().__str__() + " ~ "+ msg

    def calcArea(self):
        area = self.__width * self.__height
        return area

    def calcPerimeter(self):
        result = 2 * self.__width + 2 * self.__height

def main():

    rhombus = Shape("Rhombus")
    print(rhombus)
    rArea = rhombus.calcArea()
    print("Area:", rArea)

    rect = Rectangle("Rectangle", 4, 5)
    print(rect)
    area = rect.calcArea()
    print("Area", area)

main()