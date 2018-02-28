# Shamit Bhatia
# ITP 115, Fall 2016
# Lab practical L11
# Shamitbh@usc.edu

def main():

    fileIn = open("story.txt", "r")
    wordList = []
    dictionary = {}
    lineNumber = 1

    for line in fileIn:
        line = line.strip()
        # line = line.lower()
        # line = line.replace(",", "")
        # line = line.replace(".", "")
        # line = line.replace(" ", "")
        # line = line.replace("-", "")
        wordList = line.split(" ")
        for word in wordList:
            # if word NOT already in dictionary
            # add word (as key) to dictionary, and value will be line number AS A LIST
                # dictionary[word] = 1
            if word not in dictionary:
                dictionary[word] = [lineNumber]
            # else (we have seen the word before)
                #append current line number
            else:
                dictionary[word].append(lineNumber)
        lineNumber = lineNumber + 1

    print(dictionary)

    # convert the key to a list in order to sort
    keyList = list(dictionary.keys())
    keyList.sort()

    # print out concordance

    print(word, keyList)

main()