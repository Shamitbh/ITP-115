"""

create lists for parts of speech
while user wants to continue
    display menu
    ask user choice
    if choice is 1
        print all words
    eilf choice is 2
        ask user if they want to add noun or verb
            if noun
                ask for noun
                add noun to list
            if verb
                ask for verb
                add to list
    elif choice is 3
        freebie! (havent learned yet)
    elif choice is 4
        print out sentence
    elif choice is 5
        print exiting
    else
        print invalid choice

"""
import random



articles = ["a", "the"]
nouns = ["parrot", "carrot", "ferret"]
verbs = ["swims", "bikes", "runs"]

choice = 0 # user menu option
subChoice = 0 # user choice of verb or noun

while(choice != 5):
    print("Welcome to the Sentence Generator!")
    print("Menu")


    print("1) View, 2) Add, 3) Remove, 4) Generate Sentence, 5) Exit")
    choice = int(input(">> "))

    if (choice == 1): #view words
        print("Articles: ",articles)
        print("Nouns: ",nouns)
        print("Verbs: ",verbs)
    elif (choice == 2):
        subChoice = int(input("Press 1 for noun or 2 for verb: "))
        word = input("Enter your word")
        if (subChoice == 1):
            nouns.append(word)
        elif (subChoice == 2):
            verbs.append(word)
        else:
            print("Invalid choice")

       # print("add words")
    elif (choice == 3):
        print("remove words")
        articles.clear()
        nouns.clear()
        verbs.clear()
    elif (choice == 4):
        # format: ARTICLE NOUN VERB ARTICLE NOUN
        print(random.choice(articles),
              random.choice(nouns),
              random.choice(verbs),
              random.choice(articles),
              random.choice(nouns))
        print("generate sentence")
    elif (choice == 5):
        print("Now exiting")
    else:
        print("Invalid")

