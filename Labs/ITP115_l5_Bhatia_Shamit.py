# Shamit Bhatia
# ITP 115, Fall 2016
# Lab practical L5
# Shamitbh@usc.edu

# Get two sentences from user
string1 = input("Please enter a word or statement: ")
string2 = input("Please enter a second word or statement: ")

# Convert to lowercase
lower1 = string1.lower()
lower2 = string2.lower()

# Remove the spaces
noSpaces1 = lower1.replace(" ","")
noSpaces2 = lower2.replace(" ","")

# Convert words to lists
list1 = list(noSpaces1)
list2 = list(noSpaces2)

# Check if they are anagrams
list1.sort()
list2.sort()

print(list1)
print(list2)

    # Sort alphabetically and compare
if list1 == list2:
    print("\nThe two words you entered are anagrams!")
else:
    print("\nThe two words you entered are NOT anagrams!")

# Check if each sentence is a palindrome
    # Use a for loop
# First sentence
pal1 = list(noSpaces1)
isPal1 = True
lastIndex1 = len(pal1) - 1 # Amount of indexes

for index1 in range(len(pal1)):
    # check the letter
    if pal1[index1] != pal1[lastIndex1 - index1]:
        #letters don't match
        isPal1 = False
if isPal1:
    print("The first word is a Palindrome!")
else:
    print("The first word is NOT a palindrome!")

# Second Sentence
pal2 = list(noSpaces2)

isPal2 = True
lastIndex2 = len(pal2) - 1 # amount of indexes

for index2 in range(len(pal2)):
    # check the letter
    if pal2[index2] != pal2[lastIndex2 - index2]:
        #letters don't match
        isPal2 = False
if isPal2:
    print("The second word is a Palindrome!")
else:
    print("The second word is NOT a palindrome!")