# # Files Overview #
#
# # File - collection of information (data in bytes)
#     # Stored as either test (.txt) (.html) or Binary (.jpg) (.mp3)
#
# # Reading from file
#     # Process of getting data FROM a file already on your computer
#
# # 1) Open a file
#     # open()
#     # fileIn = open("words.txt", "r")
#         # parameters (name of file, file access mode (read or write mode))
#
# # 2) Reading from a File
# fileIn = open("words.txt", "r")
# for line in fileIn:
#     print(line)
#     # But output produced has extra line breaks b/c in words.txt file each line has invisible \n
#     # To get around this use someString.strip(), which removes all blank spaces on ends of line
#     for line in fileIn:
#         line = line.strip()
#         print(line)
#
# # 3) Close the file
# fileIn = open("words.txt", "r")
# for line in fileIn:
#     line = line.strip()
#     print(line)
# fileIn.close()
#
# # If we had file of ints, need to cast line to an int
# for line in fileIn:
#     line = int(line.strip())
#     print(2*line)
#
#
# count = 1
# print(count % 2)
#
# board_list = ["0","1","2","3","4","5","6","7","8"]
#
# def main():
#     playerSpot = input("Choose a spot: ")
#
#     while (isValidMove(board_list,playerSpot) != True):
#         print("Invalid. enter again.")
#         playerSpot = input("Choose a spot: ")
#         isValidMove(board_list,playerSpot)
#
#     print(int(playerSpot)+1)
# def isValidMove(board_list, spot):
#
#     #return boolean value true if spot is open or false if spot already taken/out of range
#     if spot in board_list:
#         return True
#     else:
#         return False
#
# main()

i = 2
j = 9
k = "3"
x = 3.0
y = 2.5
h = "hello"
print(j % i) #1
print(k*i) #prints out 3 2x, so 33
print(j / i) # 4.5
print(j // i) # 4
print(x * y) # 7.5