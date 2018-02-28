# Shamit Bhatia
# Sentence Generator



def menu():
    print("Welcome to Sentence Generator")
    print("Menu")
    print("1) View Words")
    print("2) Add Words")
    print("3) Remove Words")
    print("4) Generate sentence")
    print("5) Exit")

def main():
    articles = ['a', 'the']
    nouns = ['person', 'place', 'thing']
    verbs = ['danced', 'ate', 'froliced']

    keepGoing = False
    while(not keepGoing):
        print(menu())
        choice = input("\n")
        if (choice == "1"):
            print(articles)
            print(nouns)



            print(verbs)
        elif (choice == "2"):
            print("Adding...")
            addWord = input("What word should I add to nouns? ")
            nouns.append(addWord)
        elif (choice == "3"):
            nouns.remove("person")
            print(nouns)
        elif (choice == "5"):
            keepGoing = True

main()

