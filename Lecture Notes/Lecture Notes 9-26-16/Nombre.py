# Play with names.txt

# Define main
def main():
    # load names from file
    names = loadNames()

    #display a menu and loop through asking for user choice

    user = "y"
    while user != "n":
        displayMenu()
        choice = int(input(">"))
        if choice == 1:
            displayNames(names)
        elif choice == 2:
            addName(names)
        elif choice == 3:
            removeName(names)
        else:
            print("Please enter a 1, 2 or 3.")
        user = input("Do you want to continue (y/n)?")
        user = user.lower()

    # save names to file
    saveNames(names)


# Load the names from a file
# Output: a list containing the names
def loadNames():
    namesList = []

    # Open file
    fileIn = open("names.txt", "r")

    # Read from file
    for line in fileIn:
        line = line.strip()
        namesList.append(line)


    # Close file
    fileIn.close()

    return namesList


# Save the names to a file
# Input: a list of names
def saveNames(listOfNames): # can be namesList but doesn't have to be

    # Open file for writing
    fileOut = open("names.txt","w")

    # Print to the file
    # Loop through the list of names
    for item in listOfNames:
        print(item, file=fileOut)

    # Close the file
    fileOut.close()
    print("Saved names to names.txt")


# Display names
def displayNames(namesToDisplay):
    print(namesToDisplay)


# Add a name
def addName(namename):
    name = input("Enter a new name to add: ")
    name = name.strip()
    if name:
        namename.append(name)

    return namename

# Remove a name
# Input: a list of names
def removeName(listToDeleteFrom):
    deleteName = input("Enter a name to delete: ")
    if deleteName in listToDeleteFrom:
        listToDeleteFrom.remove(deleteName)
    else:
        print("That name is not in the list.")

    return listToDeleteFrom

# Display menu
def displayMenu():
    print("Please enter your choice:")
    print("1 --> Display Names")
    print("2 --> Add Name")
    print("3 --> Remove Name")


# Call main
main()