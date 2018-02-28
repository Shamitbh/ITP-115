# Lists are mutable
# Can make slices i.e [1:4] goes to number - 1

nums = [3, -12, 5]

nums[0] = 46 # now list is [46,-12,5]

nums[0:2] = [7,9] #subsitute 0 and 1 index as 7 and 9 -> list is now [7,9,5]

nums[0:2] = [13] # now list is [13,5]

# List Methods:
# someList.append(value) #Adds value to end of a list
# someList.sort() #Sorts elements, smallest value first

# newList = list(someString)
# Example:
# word = "hello"
# letterList = list (word)
# print(word)
# # prints "hello"
# print(letterList)
# print ['h', 'e', 'l', 'l', 'o']

# Delimeters:
# wordList = ["Hello", "My","Name","is","Shamit"]
# delimeter = " "
# quote = delimeter.join(wordList)
# print (quote)
# prints out "Hello My Name is Shamit"

