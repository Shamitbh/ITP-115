# Shamit Bhatia
# ITP 115, Fall 2016
# Assignment 10
# Shamitbh@usc.edu
# Purpose: Use inheritance to model interactions between a vampire and humans

from Human import Human
from Vampire import Vampire


def main():

    # create a list of human objects
    humanList = []

    human1 = Human("Eric Brooks", 5, "A-")
    humanList.append(human1)

    human2 = Human("Mina Harker", 7, "O+")
    humanList.append(human2)

    human3 = Human("Louis de Pointe du Lac", 4, "O+")
    humanList.append(human3)

    human4 = Human("Annie Sawyer", 3, "B-")
    humanList.append(human4)

    # Create a vampire object using user input
    vampireName = input("Please enter a name for the Vampire: ")
    vampireAnimal = input("Please enter an animal: ")

    vampireObj = Vampire(vampireName, 0, vampireAnimal)

    while True:
        printMenu()
        menuChoice = input()
        while menuChoice != "1" and menuChoice != "2" and menuChoice != "-1":
            print("Error, please try again!")
            printMenu()
            menuChoice = input()
        if menuChoice == "1":
            # print all humans
            printHumans(humanList)
        elif menuChoice == "2":
            # suck blood
            printHumans(humanList)
            performFeeding(humanList,vampireObj)
        else:
            break
    print()
    print(vampireObj.getName(),"transformed back into a(n)",vampireObj.getAnimal())

# create function for displaying menu (practice use of funcs.)
def printMenu():
    print()
    print("Menu:")
    print("1  --> Print All Humans")
    print("2  --> Suck Blood")
    print("-1 --> Quit")
    print("Enter your choice: ",end="")

def printHumans(humanList):
    print()
    for item in range(len(humanList)):
        print(str(item)+ ") "+str(humanList[item]))

def performFeeding(humanList,vampireObj):
    humanIndex = int(input("Please select a human from the list: "))
    # error check
    while humanIndex != 0 and humanIndex!= 1 and humanIndex != 2 and humanIndex != 3:
        print("Error, please try again:")
        printHumans(humanList)
        humanIndex = int(input("Please select a human from the list: "))
    if humanList[humanIndex].isAlive() and not vampireObj.isStuffed():
        vampireObj.suckBlood(humanList[humanIndex])
        print(humanList[humanIndex])
        print(vampireObj)
    elif not humanList[humanIndex].isAlive():
        print("Human",humanList[humanIndex].getName(),"is dead! Cannot suck blood.")
        print(vampireObj)
    elif vampireObj.isStuffed():
        print(humanList[humanIndex])
        print(vampireObj)
        print(vampireObj.getName(),"cannot suck any more blood!")





main()