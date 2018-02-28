from Scrabble import Scrabble

def main():

    # Read from file
    wordList = readFromFile("words.txt")

    # make scrabble object
    scrabbleObj = Scrabble(wordList)

    while True:
        # Display menu
        displayMenu()
        menuChoice = input()
        print()
        if menuChoice != "1" and menuChoice != "2" and menuChoice != "3" \
                and menuChoice != "4" and menuChoice != "5" and menuChoice != "6" \
                and menuChoice != "7" and menuChoice != "8":
            break
        if menuChoice == "1":
            # Verify if word exists in dictionary
            word = input("Please enter a word to check if "
                         "it exists in the dictionary: ")
            if (scrabbleObj.wordVerifier(word)):
                print(word.lower(),"was found in the Dictionary!")
            else:
                print(word.lower(),"was not found in the Dictionary!")
        if menuChoice == "2":
            # Display all 2 letter words
            print("List of all two-letter words in the the Dictionary:")
            print("---------------------------------------------------")
            scrabbleObj.displayTwoLetters()
        if menuChoice == "3":
            # Display words starting with Q but not followed by U
            print("List of words that start with Q but are NOT "
                  "followed by U in the Dictionary:")
            print("----------------------------------------------------------------------------")
            scrabbleObj.displayQWords()
        if menuChoice == "4":
            # Show words given an input set of tiles
            tiles = input("Please enter a set of tiles (letters): ")
            tilesLength = len(tiles)
            print()
            print("List of words that can be made with",tiles+":")
            print("-------------------------------------", end="")
            for i in range(tilesLength):
                print("-", end="")
            print()
            scrabbleObj.displayWordsGivenTiles(tiles)
        if menuChoice == "5":
            # Show anagrams given an input set of tiles
            tiles = input("Please enter a set of tiles (letters): ")
            while len(tiles) <= 1:
                print("Incorrect input!")
                tiles = input("Please enter a set of tiles (letters): ")
            tilesLength = len(tiles)
            print()
            print("List of words that are anagrams of",tiles+":")
            print("------------------------------------", end="")
            for i in range(tilesLength):
                print("-", end="")
            print()
            scrabbleObj.displayAnagrams(tiles)
        if menuChoice == "6":
            # Show all 3-letter words given an input tile
            tile = input("Please enter a tile (letter): ")
            while len(tile) > 1:
                print("Incorrect input!")
                tile = input("Please enter a tile (letter): ")
            print()
            print("List of three-letter words containing",tile+":")
            print("----------------------------------------")
            scrabbleObj.displayThreeLetter(tile)
        if menuChoice == "7":
            # Show words containing letters X or Z and the input tile
            tile = input("Please enter a tile (letter): ")
            while len(tile) > 1 or tile == "z" or tile == "x":
                print("Incorrect input!")
                if tile == "z" or tile == "x":
                    print("Please enter a letter other than Z or X")
                tile = input("Please enter a tile (letter): ")
            print()
            print("List of words containing",tile.upper(),"and either the letter Z or X:")
            print("--------------------------------------------------------")
            scrabbleObj.displayXorZ(tile)
        if menuChoice == "8":
            # Show words beginning with an input set of tiles
            tiles = input("Please enter one or more tiles (letters): ")
            tilesLength = len(tiles)
            print()
            print("List of words starting with",tiles+":")
            print("-----------------------------", end="")
            for i in range(tilesLength):
                print("-", end="")
            print()
            scrabbleObj.beginWord(tiles)

    print()
    print("Thank you for using Scrabbler!")
def displayMenu():
    print()
    print("Welcome to the Python Scrabbler program")
    print("1) Verify the word")
    print("2) Display all 2-letter words")
    print("3) Display words starting with Q but not followed by U")
    print("4) Show words given an input set of tiles")
    print("5) Show anagrams given an input set of tiles")
    print("6) Show all 3-letter words given an input tile")
    print("7) Show words containing letters X or Z and the input tile")
    print("8) Show words beginning with an input set of tiles")
    print("Press any other key to exit")
    print("Enter your choice: ", end="")

def readFromFile(fileName):
    fileIn = open(fileName, "r")
    wordList = []
    for line in fileIn:
        line = line.strip()
        wordList.append(line)
    return wordList




main()