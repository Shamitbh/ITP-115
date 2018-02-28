# Shamit Bhatia
# 09/28/2017
# Tic Tac Toe

import TicTacToeHelper

def isValidMove(boardList, spot):
    spot = str(spot)
    if spot in boardList:
        return True
    else:
        return False


def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter

def playGame():
    boardList = ['0','1','2','3','4','5','6','7','8']
    counter = 0

    playerLetter = "x"
    # keep looping until x wins, o wins, or stalemate
    while TicTacToeHelper.checkForWinner(boardList, counter) != "x" and \
                    TicTacToeHelper.checkForWinner(boardList, counter) != "o" and TicTacToeHelper.checkForWinner(boardList, counter) != "s":
        # play the game
        TicTacToeHelper.printUglyBoard(boardList)
        spot = int(input("Player "+playerLetter+", pick a spot: "))
        valid = isValidMove(boardList,spot)
        while valid != True:
            print("Invalid move, try again.")
            spot = int(input("Player " + playerLetter + ", pick a spot: "))
            valid = isValidMove(boardList, spot)

        # now the spot is valid, so update board
        updateBoard(boardList, spot, playerLetter)

        # change player type
        if playerLetter == "x":
            playerLetter = "o"
        else:
            playerLetter = "x"

    # at this point, theres a winner
    if TicTacToeHelper.checkForWinner(boardList, counter) == "x":
        print("Player x wins!")
    elif TicTacToeHelper.checkForWinner(boardList, counter) == "o":
        print("Player o wins!")
    else:
        print("Stalemate")

def main():
    playGame()

main()