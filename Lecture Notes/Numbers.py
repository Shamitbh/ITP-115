# uses numbers.txt
# file reading

def main():
    # 3 steps
    # 1) open a file
    fileIn = open("numbers.txt","r")

    # 2) read data
    counter = 0
    sum = 0
    for line in fileIn:
        line = line.strip()
        num = float(line)
        sum = sum + num
        counter = counter + 1

    # 3) close file
    fileIn.close()

    # display info

    print("Count = ",counter)
    print("Sum = ",sum)
    average = sum / counter
    print("Average = ",average)

main()