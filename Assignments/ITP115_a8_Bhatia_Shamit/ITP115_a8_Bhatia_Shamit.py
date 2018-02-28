# Shamit Bhatia
# ITP 115, Fall 2016
# Assignment 8
# Shamitbh@usc.edu
# Purpose: Create an Animal Daycare program making use of objects.

def main():

    print("Welcome to the Animal Daycare! Here is what we can do:")

    animalListMain = loadAnimals("animals.csv")

    # loop through menu
    loopControl = True

    while (loopControl):
        displayMenu()
        choice = input("\n\nPlease make a selection: ")
        if (choice == "7"):
            break
        elif (choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice!= "8"):
            print("*Invalid selection, please try again.")
            continue
        elif (choice == "1"):
            # play with animal
            animalChoice = selectAnimal(animalListMain)
            animalChoice.play()
            print("You played with", animalChoice.name,"the",animalChoice.species)
        elif (choice == "2"):
            # feed animal
            animalChoice = selectAnimal(animalListMain)
            animalChoice.feed()
            print("You fed", animalChoice.name, "the", animalChoice.species)
        elif (choice == "3"):
            # Give medicine to animal
            animalChoice = selectAnimal(animalListMain)
            animalChoice.giveMedicine()
            print("You gave", animalChoice.name, "the", animalChoice.species,"some medicine!")
        elif (choice == "4"):
            # make animal sleep
            animalChoice = selectAnimal(animalListMain)
            animalChoice.sleep()
            print(animalChoice.name, "the", animalChoice.species,"took a nap")
        elif (choice == "5"):
            # Print an Animal's stats
            animalChoice = selectAnimal(animalListMain)
            print(animalChoice)
        elif (choice == "6"):
            # View all animals
            for i in range(0,len(animalListMain)):
                print(animalListMain[i])
        # else:
        #     # Extra Credit
        #     saveAnimals("test.txt",animalListMain)

    print("Goodbye! Have a nice day")

class Animal(object):
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        self.hunger = int(hunger)
        self.happiness = int(happiness)
        self.health = int(health)
        self.energy = int(energy)
        self.age = int(age)
        self.name = name
        self.species = species

    def play(self):
        self.happiness += 10
        self.hunger += 5
        if self.happiness <= 0:
            self.happiness = 0
        if self.happiness >= 100:
            self.happiness = 100
        if self.hunger <= 0:
            self.hunger = 0
        if self.hunger >= 100:
            self.hunger = 100

    def feed(self):
        self.hunger -= 10
        if self.hunger <= 0:
            self.hunger = 0
        if self.hunger >= 100:
            self.hunger = 100

    def giveMedicine(self):
        self.happiness -= 20
        self.health += 20
        if self.happiness <= 0:
            self.happiness = 0
        if self.happiness >= 100:
            self.happiness = 100
        if self.health <= 0:
            self.health = 0
        if self.health >= 100:
            self.health = 100

    def sleep(self):
        self.energy += 20
        self.age += 1
        if self.energy <= 0:
            self.energy = 0
        if self.energy >= 100:
            self.energy = 100


    def __str__(self):
        msg = ("Name: "+self.name+" the "+self.species)
        msg += ("\nHealth: "+str(self.health))
        msg += ("\nHappiness: "+str(self.happiness))
        msg += ("\nHunger: "+str(self.hunger))
        msg += ("\nEnergy: "+str(self.energy))
        msg += ("\nAge: "+str(self.age))
        msg += ("\n*********************************")

        return msg


def displayMenu():
    # print entire menu
    print("\n1) Play")
    print("2) Feed")
    print("3) Give Medicine")
    print("4) Sleep")
    print("5) Print an Animal's stats")
    print("6) View All Animals")
    print("7) Exit")

def loadAnimals(fileName):

    fileIn = open(fileName,"r")

    bigList = []
    animalList = []

    # read through csv file
    for line in fileIn:
        line = line.strip()
        smallList = line.split(",")
        bigList.append(smallList)

        #create animal object
        animalObj = Animal(smallList[0],smallList[1],smallList[2],smallList[3],smallList[4],smallList[5],smallList[6])

        # Append each animal object to animalList
        animalList.append(animalObj)

    fileIn.close()

    return animalList

    #return a list of animal instance variables

def selectAnimal(animalListMain):

    print("1)",animalListMain[0].name,"the",animalListMain[0].species)
    print("2)",animalListMain[1].name,"the",animalListMain[1].species)
    print("3)",animalListMain[2].name,"the",animalListMain[2].species)
    print("4)",animalListMain[3].name,"the",animalListMain[3].species)
    print("5)",animalListMain[4].name,"the",animalListMain[4].species)

    choice = input("\nPlease select an animal from the list (enter 1-5): ")
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("Invalid input, please try again!")
        choice = input("Please select an animal from the list (enter 1-5): ")

    # need to match choice with index for animalListMain
    userChoiceIndex = int(choice) - 1

    return animalListMain[userChoiceIndex]


# def saveAnimals(fileName, animalList):
#
#     fileOut = open(fileName, "w")
#     print("Hello world\n\n",file=fileOut)
#
#     for i in range(0, len(animalList)):
#         print("Hi ppl",file=fileOut)
#         print(animalList[i].name+animalList[i].species,file=fileOut)
#
#     fileOut.close()

main()