# Shamit Bhatia
# ITP 115, Fall 2016
# Assignment 6
# Shamitbh@usc.edu
# Purpose: Create a program that parses through CSV files and writes to text files



# Main Function
def main():
    displayMenu()
    yearChoice = whichYearFile()
    while yearChoice != "2008" and yearChoice != "2009":
        print("Invalid input, please try again!")
        yearChoice = whichYearFile()
    #print(yearChoice)
    yearChoiceFile = "epaVehicleData"+yearChoice+".csv"
    #print(yearChoice)
    fileWrite = askUserFileName()
    # print(fileWrite)

    carListMax = readFromFileMax(yearChoiceFile)
    maxValue = carListMax[4]
    car1 = carListMax[0]
    car1Type = carListMax[2]
    car2 = carListMax[1]
    car2Type = carListMax[3]

    WriteToFile(fileWrite,yearChoice,maxValue,car1,car1Type,car2,car2Type)

    print("Operation success!")

def displayMenu():
    print("Welcome to EPA Mileage Calculator\n")


# Input: None
# Output: None
# Purpose: Ask user which file year to read from
def whichYearFile():
    choice = input("What year would you like to view data for? (2008 or 2009): ")
    return choice

def askUserFileName():
    fileName = input("Enter the filename to save the results to: ")
    return fileName


def readFromFileMax(fileName):
    fileIn = open(fileName,"r")
    bigList = []
    for list1 in fileIn:
        list1 = list1.strip()
        smallList = list1.split(",")
        bigList.append(smallList)
        lineCounter = 0
        if lineCounter == 0:
            for item in smallList:
                if item == "HWY MPG (GUIDE)":
                    headerIndex = smallList.index("HWY MPG (GUIDE)")

    # print(headerIndex)

    maxVal = 0 # arbitrary number to be able to compare future values
    for item in bigList:
        if item[headerIndex] != "HWY MPG (GUIDE)":
            if int(item[headerIndex]) > maxVal:
                maxVal = int(item[headerIndex])
    carList1 = []
    carList2 = []
    for item in bigList:
        if item[headerIndex] != "HWY MPG (GUIDE)":
            if int(item[headerIndex]) == maxVal:
                carList1.append(item[1])
                carList2.append(item[2])
    # print(carList1)
    # print(carList2)
    carList1.append(carList2[0])
    carList1.append(carList2[1])
    carList1.append(maxVal)

    # print(carList1)
    return carList1

#
# def readFromFileMin(fileName):
#     fileIn = open(fileName, "r")
#     bigList = []
#     for list1 in fileIn:
#         list1 = list1.strip()
#         smallList = list1.split(",")
#         bigList.append(smallList)
#         lineCounter = 0
#         if lineCounter == 0:
#             for item in smallList:
#                 if item == "HWY MPG (GUIDE)":
#                     headerIndex = smallList.index("HWY MPG (GUIDE)")
#
#     minVal = 500 # arbitrary number to be able to compare future values
#     for item in bigList:
#         if item[headerIndex] != "HWY MPG (GUIDE)":
#             if int(item[headerIndex]) < minVal:
#                 minVal = int(item[headerIndex])
#     carList1 = []
#     carList2 = []
#     for item in bigList:
#         if item[headerIndex] != "HWY MPG (GUIDE)":
#             if int(item[headerIndex]) == minVal:
#                 carList1.append(item[1])
#                 carList2.append(item[2])
#     print(minVal)
#     print(carList1)
#     print(carList2)
#     carList1.append(carList2[0])
#     carList1.append(carList2[1])
#
#     print(carList1)
#     return carList1




    # maxVal = 0
    # for i in range(1,len(mpgList)):
    #     if int(mpgList[i]) > maxVal:
    #         maxVal = int(mpgList[i])
    #         index = i
    # print(index)
    # print(maxVal)

    # print(mpgList)
    # print(bigList)


def WriteToFile(fileName,yearChoice,max,car1,car1Type,car2,car2Type):
    fileOut = open(fileName,"w")

    print("EPA Highway Mileage Calculator: "+yearChoice, file=fileOut)
    print("----------------------------------------", file=fileOut)
    print("Maximum mileage (highway):",max, file=fileOut)
    print("\t"+car1+" "+car1Type, file=fileOut)
    print("\t"+car2+" "+car2Type, file=fileOut)

    # print("Minimum mileage (highway):",min, file=fileOut)

main()