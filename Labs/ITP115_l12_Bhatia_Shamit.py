# Shamit Bhatia
# ITP 115, Fall 2016
# Lab 12
# Shamitbh@usc.edu

import random

def main():

    choice1 = input("Do you want to use a default dice for your first dice (y/n):? ")
    if choice1 == "y":
        dice1 = Die()
    elif choice1 == "n":
        choice2 = int(input("How many sides would you like for your first dice? "))
        dice1 = Die(choice2)

    choice3 = input("Do you want to use a default dice for your second dice (y/n):? ")
    if choice3 == "y":
        dice2 = Die()
    elif choice3 == "n":
        choice4 = int(input("How many sides would you like for your second dice? "))
        dice2 = Die(choice4)

    roll1 = dice1.roll()
    roll2 = dice2.roll()

    diceSum = findSum(roll1,roll2)

    print("Dice 1 rolled a", roll1)
    print("Dice 2 rolled a", roll2)
    choiceRolls = int(input("How many rolls?"))

    print("The sum is", diceSum)
    print("The average is", findSumAverage(dice1, dice2, choiceRolls))

def findSum(dieNum1, dieNum2):
    sum = dieNum1 + dieNum2
    return sum

def findSumAverage(dieNum1, dieNum2, numRolls):
    total = 0
    for i in range(numRolls):
        roll1 = dieNum1.roll()
        roll2 = dieNum2.roll()
        total += roll1 + roll2
    return total/numRolls

class Die (object):
    def __init__(self, numSides = 6):
        self.mNumSides = numSides
        self.mResult = 0

    def roll(self):
        self.mResult = random.randrange(1, self.mNumSides+1)
        return self.mResult

    def __str__(self):
        msg = str(self.mResult)
        return msg

main()
