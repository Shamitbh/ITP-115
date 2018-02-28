# Part 1: Jumbled game
#
# import random
#
# listSports = ["basketball", "baseball", "football", "soccer", "golf"]
#
# randomWord = random.choice(listSports)
#
# firstWord = randomWord
#
# listRandomWord = list(randomWord)
#
# jumbledList = []
#
# while len(listRandomWord) > 0:
#     # get random letter in the word
#     randomLetter = random.choice(listRandomWord)
#     # append random letter to new jumbled word
#     jumbledList.append(randomLetter)
#     # remove the letter from original word so that letter not chosen again
#     listRandomWord.remove(randomLetter)
#
# jumbledString = "".join(jumbledList)
#
# print("The jumbled word is",jumbledString)
#
# isContinue = True
# numTries = 0
# while isContinue == True:
#     guess = input("Please enter your guess: ")
#     if guess.lower() != randomWord:
#         print("Try again")
#     else:
#         print("You got it!")
#         isContinue = False
#
#     numTries += 1
#
# print("It took you",numTries,"tries")


# Part 2: Encrypt/Decrypt

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cipher = []

message = input("Please enter a message: ")
shift = int(input("Please enter a number to shift by: "))

# make cipher shifted

cipher = alphabet[shift:] + alphabet[:shift]
print(alphabet)
print(cipher)

wordInListForm = []

# go thru message and see where that index lines up with cipher index and return letter from cipher or append it to a big list
for letter in message:
    if letter not in alphabet:
        wordInListForm.append(letter)
        continue
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            wordInListForm.append(cipher[i])


wordInStringForm = "".join(wordInListForm)
print(wordInListForm)
print(wordInStringForm)