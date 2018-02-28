# Shamit Bhatia
# ITP 115, Fall 2016
# Assignment 4
# Shamitbh@usc.edu


# PART 1: JUMBLED WORD

import random

totalFruitList = ["orange","banana","apple","peach","grape"]

# Pick a random fruit from totalFruitList
fruitString = random.choice(totalFruitList)

# Make the word (random fruit) into a list
fruitList = list(fruitString)

jumbledFruit = ""

# Iterate through list to get random letters from fruitList
while len(fruitList) > 0:
    randomLetter = random.choice(fruitList) # Gets 1 random letter from fruitList
    fruitList.remove(randomLetter) # Remove the random letter that was selected, making fruitList smaller as a whole
    jumbledFruit = jumbledFruit + randomLetter # Put random letter into new jumbledFruit

# Check if user enters correct word with loop
print("The jumbled word is:",jumbledFruit)
userGuess = input("Please enter your guess (capitalization doesn't matter): ")
counter = 1 # keep track of guesses -> set to 1 b/c of initial guess

while userGuess.lower() != fruitString:
    counter = counter + 1
    print("Try Again.")
    userGuess = input("Please enter your guess (capitalization doesn't matter): ")
print("\nYou got it! You're a genius.")
print("It took you",counter,"guess(es).")


# PART 2: CEASAR CIPHER

# Initialize the two lists (english alphabet / ceasar cipher)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cipher = []

userMessage = input("\n\nEnter a message: ")
userMessage = userMessage.lower()

shift = int(input("Enter a number to shift by (0-25): "))
cipher = alphabet[shift:] + alphabet[:shift] # makes new list (cipher) that's shifted by user number

encryptedMessage = ""

# Iterate through user entered message and see if index is same as alphabet
for letter in userMessage:
    if letter in alphabet:
        newLetterIndex = alphabet.index(letter) # stores the value at the specified index in alphabet
        encryptedMessage = encryptedMessage + cipher[newLetterIndex] # add the value at cipher[index] to encryptedMes.
    else:
        encryptedMessage = encryptedMessage + " "

print("\n\nEncrypting message . . . .")

if "." in userMessage:
    encryptedMessageList = list(encryptedMessage)
    del encryptedMessageList[len(encryptedMessageList)-1]
    encryptedMessagePeriod = "".join(encryptedMessageList)
    print("\tEncrypted message: "+encryptedMessagePeriod+".")
else:
    print("\tEncrypted message:", encryptedMessage)

decryptedMessage = ""

# Iterate throguh encryptedMessage to get back to original message
for letter in encryptedMessage:
    if letter in alphabet:
        newLetterIndex = cipher.index(letter) # stores the value at the specified index in cipher
        decryptedMessage = decryptedMessage + alphabet[newLetterIndex] # add value at alphabet[index] to decryptedMes.
    else:
        decryptedMessage = decryptedMessage + " "

# See if original message had punctuation (periods)
print("Decrypting message . . . .")
if "." in userMessage:
    decryptedMessageList = list(decryptedMessage)
    del decryptedMessageList[len(decryptedMessageList)-1]
    decryptedMessagePeriod = "".join(decryptedMessageList)
    print("\tDecrypted message: "+decryptedMessagePeriod+".")
else:
    print("\tDecrypted message:", decryptedMessage)

print("\tOriginal message:",userMessage)