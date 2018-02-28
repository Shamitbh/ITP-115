
def main():


    # get filename from user
    fileName = input("Enter a pokemon file: ")

    # open the file
    fileIn = open(fileName, "r")

    # read file
    count = 0

    pokemonList = []




    for line in fileIn:
        line = line.strip()
        # print(line)
        count += 1
        if line[0].lower() == "p":
            pokemonList.append(line)

    # close file
    fileIn.close()

    # display info
    print("There are",count,"pokemon in the file")
    print("There are", len(pokemonList), "pokemon that start with P.")
    print(pokemonList)

main()