# Shamit Bhatia
# ITP 115, Fall 2016
# Lab L9
# Shamitbh@usc.edu

def main():
    print("Welcome to the spell checker! ")

    dictionaryTxt = input("Please enter the dictionary file you wish to read in: ")
    passageTxt = input("Please enter the text file you wish to read in: ")

    dictionary = readDictionaryFile(dictionaryTxt)
    text = readTextFile(passageTxt)


    mispelled = findErrors(dictionary, text)

    printErrors(mispelled)


def readDictionaryFile(dictionaryFileName):
    dictionaryList = []
    dictionaryFile = open(dictionaryFileName, "r")
    for line in dictionaryFile:
        line = line.strip()
        dictionaryList.append(line)
    dictionaryFile.close()

    # output
    return dictionaryList

def readTextFile(textFileName):
    textList = []
    textFile = open(textFileName, "r")
    for line in textFile:
        line = line.strip()
        lineSplit = line.split()
        for word in lineSplit:
            word = word.strip(" .,\":;?")
            word = word.lower()
            textList.append(word)

    textFile.close()

    return textList

def findErrors(dictionaryList, textList):
    errorList = []
    for word in textList:
        if word not in dictionaryList:
            errorList.append(word)

    return errorList

def printErrors(errorList):
    print("The mispelled words from the file are: ")
    for word in errorList:
        print(word)

main()