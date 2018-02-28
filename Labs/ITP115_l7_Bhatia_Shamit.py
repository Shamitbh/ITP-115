# Shamit Bhatia
# ITP 115, Fall 2016
# Lab practical L7
# Shamitbh@usc.edu

import random

# Make constants to make 0 = rock, 1 = paper, 2 = scissors
GAME_CHOICES = ["Rock", "Paper", "Scissors"]


# Function: main
# Runs program
# input: none
# output: none
def main():
    numWins = 0
    numTies = 0
    numLosses = 0
    userWantsToContinue = True

    while (userWantsToContinue):
        displayMenu()
        player = getPlayerChoice()
        computer = getComputerChoice()
        result = playRound(computer, player)
        print("You chose", GAME_CHOICES[player])
        print("The computer chose", GAME_CHOICES[computer])
        if result == 0:
            print("You had a tie")
            numTies += 1
        elif result == 1:
            print("You won")
            numWins += 1
        else:
            print("You lost")
            numLosses += 1

        userWantsToContinue = continueGame() # since continueGame returns True/False it will be used in while loop
        if userWantsToContinue == False:
            print("\n\nYou won", numWins,"game(s).")
            print("The computer won", numLosses,"game(s).")
            print("You tied with the computer", numTies,"time(s).")

            print("\n\nThanks for Playing!")
# Function: displayMenu
# Displays start menu
# input: none
# output: none
def displayMenu():
    print("Welcome! Let's play Rock, Paper, Scissors")
    print("The rules of the game are:")
    print("\tRock smashes scissors")
    print("\tScissors cuts paper")
    print("\tPaper covers rock")
    print("\tIf both the choices are the same, it's a tie")

# Function: getComputerChoice
# Determines a random choice from computer
# input: none
# output: random int from 0-2
def getComputerChoice():
    num = random.randrange(3)
    return num

# Function: getPlayerChoice
# Asks user for an int from 0-2
# input: none
# output: random int from 0-2
def getPlayerChoice():
    choice = int(input("Press 0 for Rock, 1 for paper, or 2 for scissors"))
    return choice

# Function: playRound
# Simluates the game being played and determines a winner
# input: two integers - one representing computer choice and other representing player choice
# output: integer which determines winner

def playRound(computerChoice, playerChoice): #can name the parameters anything but should be readable
    # if tie
    if playerChoice == computerChoice:
        return 0
    # player wins
    elif (playerChoice == 0 and computerChoice == 2) or (playerChoice == 1 and
                                                                 computerChoice == 0) or (playerChoice == 2 and
                                                                                                           computerChoice == 1):
        return 1
    # computer wins
    else:
        return -1

# Function: continueGame
# Sees if user wants to play again
# input: none
# output: boolean
def continueGame():
    userChoice = input("Do you want to continue (y/n): ")
    if userChoice.lower() == "y":
        return True
    else:
        return False
    ###### Ideally, this should have a while loop to make sure user enters good input


main()
