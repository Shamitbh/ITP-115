def main():
    twoWordCities = []
    fileIn = open("cities.txt", "r")
    for line in fileIn:
        line = line.strip()
        if " " in line:
            twoWordCities.append(line)

    fileIn.close()

    fileOut = open("twoWordCities.txt", "w")
    for city in twoWordCities:
        print(city, file=fileOut)
    fileOut.close()

main()