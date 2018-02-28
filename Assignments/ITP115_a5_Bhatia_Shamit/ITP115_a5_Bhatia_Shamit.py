# Shamit Bhatia
# ITP 115, Fall 2016
# Assignment 5
# Shamitbh@usc.edu
# Purpose: Create a program that simulates a 2-player game of Tic-Tac-Toe

import TicTacToeHelper

def main():
    print("Welcome to Tic Tac Toe!")
    playAgain = True # "Do-while" loop using boolean playAgain the first iteration
    while(playAgain):
        playGame()
        userChoice = input("Would you like to play another round? (y/n): ")
        while (userChoice.lower() != "y" and userChoice.lower() != "n"):
            userChoice = input("Invalid input. Please enter again: ")
        if userChoice.lower() == "y":
            playAgain = True
        else:
            playAgain = False

    print("Goodbye!")
# Inputs: boardlist and spot = index position user places letter on
# Outputs: A boolean value
# Purpose: sees if spot where user wants to place letter is valid
def isValidMove(board_list, spot):
    ValidSpot = False
    #return boolean value true if spot is open or false if spot already taken/out of range
    if spot in board_list:
        validSpot = True
    else:
        validSpot = False
    return validSpot

# Inputs: boardList, spot, and player_letter = string representing either "x" or "o"
# Outputs: none
# Purpose: Takes current board list and places player_letter in specified spot
def updateBoard(board_list, spot, player_letter):

    board_list[int(spot)] = player_letter


# Input: none
# Output: none
# Purpose: play the tic-tac-toe game
def playGame():

    # Initialize board_list to strings with #'s 0-8
    board_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    TicTacToeHelper.printUglyBoard(board_list)
    # Use a counter to keep track of total # of moves made
    counter = 0 # Use counter to checkForWinner
    count = 0  # Use count to check which player it is
    # Use a while loop to allow each player to take turn until game ends (checkWinner function)
    check = TicTacToeHelper.checkForWinner(board_list,counter)
    while (check != "x" and check != "o" and check != "s"):
        player1 = "x"
        player2 = "o"

        if count % 2 == 0: # count is even and it's player x's turn
            playerSpot = input("Player "+player1+", pick a spot: ")
            valid = isValidMove(board_list,playerSpot)
            while valid != True:
                print("Invalid move, please try again.")
                playerSpot = input("Player " + player1 + ", pick a spot: ")
                valid = isValidMove(board_list,playerSpot)
            updateBoard(board_list,playerSpot,player1)
            TicTacToeHelper.printUglyBoard(board_list)
        else: # count is odd
            playerSpot = input("Player "+player2+", pick a spot: ")
            valid = isValidMove(board_list,playerSpot)
            while valid != True:
                print("Invalid move, please try again.")
                playerSpot = input("Player "+player2+", pick a spot: ")
                valid = isValidMove(board_list,playerSpot)
            updateBoard(board_list,playerSpot,player2)
            TicTacToeHelper.printUglyBoard(board_list)

        count = count + 1
        counter = counter + 1
        check = TicTacToeHelper.checkForWinner(board_list, counter)

    print("\nGame Over!")
    if (check == "x" or check == "o"): # check to see if someone won or stalemate reached
        print("Player",check,"is the winner!")
    else:
        print("Stalemate reached!")

main()