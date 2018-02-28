class Scrabble(object):

    # Constructor
    def __init__(self, wordList):
        self.__wordList = wordList


    # Input: None
    # Output: None
    def getWordList(self):
        return self.__wordList

    # Input: None
    # Output: None
    # Description: display all two letter words
    def displayTwoLetters(self):
        for item in self.__wordList:
            if len(item) == 2:
                print(item)

    # Input: None
    # Output: None
    # Description: List words that start "q" but not followed with "u"
    def displayQWords(self):
        for item in self.__wordList:
            if item[0] == "q":
                if item[1] != "u":
                    print(item)


    # Input: input tile
    # Output: None
    # Description: Show all 3-letter words given specific input tile
    def displayThreeLetter(self, inputTile):
        # make inputTile lowercase
        inputTile = inputTile.lower()
        for item in self.__wordList:
            # check if word is 3 letters
            if len(item) == 3:
                if inputTile in item:
                    print(item)

    # Input: set of tiles
    # Output: None
    # Description: Ask user for set of tiles and show all words
    # made with any of the letters
    def displayWordsGivenTiles(self, givenTiles):
        # make tiles string lowercase
        givenTiles = givenTiles.lower()
        # make list given input string to traverse each letter
        listString = []
        for item in givenTiles:
            listString.append(item)

        # traverse list one letter at a time and search dictionary
        # make dictList to hold words from dict. for each letter
        dictList = []
        for letter in listString:
            # check all words in big dictionary
            for item in self.__wordList:
                # if the letter contained in any words in dict
                if letter in item:
                    # append that word from big dictionary to dictList
                    dictList.append(item)

        # print out dictList in string format
        for word in dictList:
            print(word)


    # Input: set of tiles
    # Output: None
    # Description: Ask user for set of tiles and show anagrams
    # (i.e.) words made using all the letters
    def displayAnagrams(self, givenTiles):
        # make tiles string lowercase
        givenTiles = givenTiles.lower()

        # sort the given tiles string
        sortedInput = sorted(givenTiles)
        sortedInputString = ''.join(sortedInput)

        # make each word in the big dictionary sorted alphabetically
        dictList = []
        for word in self.__wordList:
            # sort each word in big dictionary
            sortedWordListForm = sorted(word)
            # change each word from list to string form
            sortedWordStringForm = ''.join(sortedWordListForm)

            # check whether sorted Word = sorted Input
            if sortedWordStringForm == sortedInputString:
                dictList.append(word)

        # print out dictList in string format
        for word in dictList:
            print(word)

    # Input: wordInput
    # Output: boolean true or false
    # Description: Word verifier - check if word exists in dictionary
    def wordVerifier(self, wordInput):
        wordInput = wordInput.lower()
        # traverse big dictionary
        for word in self.__wordList:
            # check if wordInput matches any of the words in dictionary
            if word == wordInput:
                return True
        # At this point, no word was found
        return False

    # Input: inputTiles
    # Output: None
    # Description: Ask user for input tile and
    # see if "Z" or "X" in word as well
    def displayXorZ(self, inputTile):
        inputTile = inputTile.lower()
        # traverse big dictionary
        for word in self.__wordList:
            if "z" in word or "x" in word:
                if inputTile in word:
                    print(word)

    # Input: inputTiles
    # Output: None
    # Description: Ask user to enter 1 or more letters
    # and show all words that begin with that group of letters
    def beginWord(self, inputTiles):
        inputTiles = inputTiles.lower()
        # figure out length of user Input
        lengthInput = len(inputTiles)
        # traverse big dictionary
        for word in self.__wordList:
            # make sure that word is as long or longer than input
            if len(word) >= lengthInput:
                # see if word starts with inputTiles
                if (word.startswith(inputTiles)):
                    print(word)




