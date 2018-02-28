# Shamit Bhatia
# ITP 115, Fall 2016
# Lab practical L10
# Shamitbh@usc.edu


def main():

    letterFreq = {}

    fileIn = open("gettysburg.txt","r")


    dict = {"a":0, "b": 0, "c":0, "d": 0,"e":0, "f": 0,"g":0, "h": 0,"i":0,
            "j": 0,"k":0, "l": 0,"m":0, "n": 0,"o":0, "p": 0,"q":0, "r": 0,"s":0, "t": 0,"u":0, "v": 0,
            "w": 0, "x": 0, "y": 0, "z": 0}
    # for line in fileIn:
    #     line = line.strip()
    #     line = line.lower()
    #     line = line.replace(",","")
    #     line = line.replace(".","")
    #     line = line.replace(" ","")
    #     line = line.replace("-","")
    #     for letter in line:
    #         if letter not in letterFreq:
    #             letterFreq[letter] = 1
    #         else:
    #             letterFreq[letter] = letterFreq[letter] + 1
    # fileIn.close()
    #
    # sortedKeys = list(letterFreq.keys())
    # sortedKeys.sort()
    #
    # for letter in sortedKeys:
    #     print(letter, "\t", letterFreq[letter])

    for line in fileIn:
        line = line.strip()
        listLet = list(line)
        for letter in listLet:
            if letter in dict:
                dict[letter] += 1

    sorted = list(dict.keys())
    sorted.sort()
    for key in sorted:
        print(key, " : ",dict[key])


main()