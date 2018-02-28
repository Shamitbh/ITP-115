# Shamit Bhatia
# ITP 115, Fall 2016
# Lab L4
# Shamitbh@usc.edu


print("\nWould you like to: \na) See the ASCII code for the alphabet\nb) Translate a word into its ASCII code")

choice1 = input("Select a or b: ") #choice1 either a or b (user input not case-sensitive)
while(choice1.lower() != "a" and choice1.lower() != "b"):
    print("You didn't enter a or b. Shame on you!")
    choice1 = input("Select a or b: ")
if (choice1.lower() == "a"):
    choice2 = input("\nDo you want to see the alphabet in upper (u) or lowercase (l)? ") #choice2 either u or l (case doesn't matter because (lower))
    while (choice2.lower() != "u" and choice2.lower() != "l"):
        print("**You have entered an invalid choice. Please try again.\n")
        choice2 = input("Do you want to see the alphabet in upper (u) or lowercase (l)? ")
    if (choice2.lower() == "u"):
        for alphabetLetter in range(65,91,1): #alphabetLetter is current Letter in Alphabet that number corresponds to.
            print(alphabetLetter,chr(alphabetLetter))
    else:
        for x in range(97,123,1):
            print(x,chr(x))

if (choice1.lower() == "b"): #choice b
    choice3 = input("\nEnter the word you would like to translate to ASCII: ")
    for letter in choice3: #letter tracks the current letter of the string that user entered
        numASCII = str(ord(letter)) #numASCII to track number each letter corresponds to
        print(letter.lower()+": "+numASCII) #concatenate strings together because numASCII now a string


