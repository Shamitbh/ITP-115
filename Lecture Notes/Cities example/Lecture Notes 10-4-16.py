# Midterm Review Class!

'''
This is a Multi line comment:
'''

# Break and Continue
    # for i in range(10):
    #     if i == 5:
    #         continue
    #     print(i)
        # Prints 0-4, 6-9

# # Structure
    # Some MCQ
    # Some T/F
    # Some short answer

# # Lists
#     Append
#     remove
#     del
#     sort
# #Strings
#     replace
#     join
#     split
#     upper
#     lower




# # Variables as conditions:
#
# a = 8
# if a:
#     print("This evaluted to true")
# else:
#     print("False")
#
#     # General rule: Any variable that is either 0 or empty (empty string "" or []) will evaluate to false
#         # Anything else will evaluate to true




# # Immutables vs. Mutables
# # Lists are mutable
#
# words = ["burrito", "pad thai", "hot dogs"]
# print(words)
# words[0] = "pizza"
# print(words)
#
# # Strings are not
#
# pet = "Mocha"
# print(pet)
# print(pet[1])
# # pet [1] = "a" # CANNOT DO THIS
# pet = pet.replace("o", "a")
# print(pet)




# Functions
    # Write a function called countWords
    # Count how many times a word appears in a list
    # Input: list of strings, and a string to search for
    # Output: an integer representing how many times the searched word was found

# def countWords(wordList, searchWord):
#     counter = 0
#     for word in wordList:
#         if word == searchWord:
#             counter += 1
#
#     return counter
#
# # Now write a main function to use the countWords function to create a list of words and use countWords
#     # to figure out how many times word is in wordList
#
# def main():
#     vegetables = ["celery", "carrot", "celery", "spinach", "celery", "kale"]
#     veggieWord1 = "celery"
#
#     veggieCount1 = countWords(vegetables, veggieWord1)
#     print(veggieWord1,"appears",veggieCount1,"times.")
#
#
#
# main()



# # Delimiters
# #     Character that separates elements
# msg = "hi, brandon, is, not, feeling, well"
# wordList = msg.split(",")
# for item in wordList:
#     print(item, end="")
# print()
# print(wordList)
#
# newMsg = " ".join(wordList)
# print(newMsg)


# File Reading/Writing
# def main():
#     fileIn = open("cities.txt", "r")
#     for line in fileIn:
#         line = line.strip()
#         print(line)
#
#
# main()

for i in range(0,100,10):
    print(i + 10)
