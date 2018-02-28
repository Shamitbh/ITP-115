# Shamit Bhatia
# ITP 115, Fall 2016
# Assignment 3
# Shamitbh@usc.edu



# Part 1: Translate an English word into Pig Elvish:

import random

# Welcome message

print("\n\nWelcome to the Pig Elvish translator!\n")

# Use while loop to ask user to enter word in English
repeat = True
while (repeat == True):
    engWord = input("Please enter a word in English: ")

    # Translate users word into Elvish - See parts below:
    engWordList = list(engWord) #make list as is to see capitals
    engWordBeg = engWordList[0] #See first letter in list

    if engWordBeg.isupper(): #check if capital
        EngWordCapital = True
    else:
        EngWordCapital = False

    # Take first letter word & move to end (make sure this letter becomes lower case)
    engWordList = list(engWord.lower()) #make list lowercase

    engWordMoved = engWordList[1:] + list(engWordList[0].lower()) #move first letter to end

    # If word >= 4 letters, append random vowel to end (aeiou)
    vowelList = ["a","e","i","o","u"]
    if (len(engWordMoved) >= 4):
        randomVowel = (random.choice(vowelList))
        engWordMoved.append(randomVowel)
        # print(engWordMoved)

    # If word <= 3 letters, append "en" to end of word
    else:
        engWordMoved.append("e")
        engWordMoved.append("n")
        # print(engWordMoved)

    # Change all k's to c's
    index = 0;
    for letter in engWordMoved:
        if engWordMoved[index] == "k":
            engWordMoved[index] = "c"
        index += 1

    # If there's e at the end of word, replace e with e (umlaut)
    eUmlaut = "ë"
    if (engWordMoved[len(engWordMoved)-1] == "e"):
        engWordMoved[len(engWordMoved)-1] = eUmlaut  # replace e with e-umlaut in list

    # Capitalize new first letter of Pig Elvish word
    stringEngWordMoved = ''.join(engWordMoved)  # convert list to string so we can use capitalize

    if (EngWordCapital):
        elvishWordFinal = stringEngWordMoved.capitalize()
        print("'"+engWord+"' in elvish is:", elvishWordFinal)
    else:
        print("'"+engWord+"' in elvish is:", stringEngWordMoved)

    # ask user if they want to continue
    question = input("\nWould you like to translate another word? (y/n)\n")
    if question.lower() == "n":
        break
    while (question.lower() != "y" and question.lower() != "n"):
        newQuestion = input("You entered an invalid choice. Please enter again (y/n): \n")
        if newQuestion.lower() == "y":
            repeat = True
            break
        elif newQuestion.lower() == "n":
            repeat = False
            break

print("\nOodbyegi! Avehë aen iceno Ayden!")
print("(Goodbye! Have a nice Day!)")




# Part 2: Find the largest number that a user enters:

repeat = True     # to have loop run
while (repeat):
    largest = 0
    print("\n\nInput an integer greater than or equal to 0 or enter -1 to quit:")

    integer = int(input("> "))
    largest = integer
    while (integer != -1): # calculate largest integer user enters
        if (integer > largest):
            largest = integer
        integer = int(input("> "))
    if (largest != -1): # check if user quits right away
        print("The largest number is", largest)
    else:
        print("The largest number wasn't computed:")
        break

    question = input("\nWould you like to find the largest number again? (y/n)\n")
    if question.lower() == "n":
        break
    while (question.lower() != "y" and question.lower() != "n"): #loop to check user error
        newQuestion = input("You entered an invalid choice. Please enter again (y/n): \n")
        if newQuestion.lower() == "y":
            repeat = True
            break
        elif newQuestion.lower() == "n":
            repeat = False
            break

print("\nGoodbye!")