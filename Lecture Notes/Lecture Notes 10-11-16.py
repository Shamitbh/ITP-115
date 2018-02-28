# Python notes: Dictionaries

# In a list, there's no real connection between the index number and the data in it

# Dictionaries
#     Store info in pairs
#     a key and its value
#         just like a real dictionary
#         word and definitino
#
# Dictionary Syntax
#     Define with { }
#     include key:value pairs separated by a ,
#
# Example
#     myDictionary = {key1:value1, key2:value2, key3:value3}
#     info = {"name":"juan","age":47,"job":"doctor"}
#     print(info["name"])
#     DICTIONARY ISNT SORTED LIKE LISTS
# Advantages of Dictionaries
#     If you had large amounts of data, retrieval should be fast
#     Logical strructure of data (key value) is more importatn than physical structure of data (memory)
#
# Dictionary Requirements
#     Keys must be unique
#         Old value will be replaced by new value
#     Keys must be immutable
#         String (numer, tuple)
#     Values do not have to be unique
#         Values can be immutable or mutable

# Create empty dictionary
# stuff = { }
# info = {
#     "name":"juan",
#     "age":47,
#     "job":"doctor"
# }
#
# print(info["age"])
#  # will print out 47
#
# Error if key is not in dictionary
# have to use key not value to get value
#
# Read through every value in dictionary
#     use for loop
#     for key in info:
#     print(info[key])
##      THE PROBLEM IS SINCE DICTIONARIES AREN'T SORTEd, WE DONT KNOW WHICH ITERATION IT STARTS AT (CANT RELY ON ORDER)


# # Adding things to Dictionary (NO APPEND)
#     info["kids"] = 2
#     info["age"] = 34  # Updates age to 34
#
# Size of dictionary
# size = len(info) # size is 4
#
# Check for keys
#     if "age" in info:
#         print("Found key age")

# Deleting keys
#   del info["kids"]




# def main():
#     films = {"Castle in the Sky":"Miyazaki",
#              "Wolf of Wall Street":"Leonardo DiCaprio",
#              "The Shawshank Redemption":"Morgan Freeman"}
#
#     newMovie = input("Enter another movie: ")
#     star = input("Enter the main actress/actor/producer: ")
#
#     films[newMovie] = star
#
#     movieToDelete = input("Enter a movie to remove: ")
#     if movieToDelete in films:
#         del films[movieToDelete]
#
#     sortedKeys = list(films.keys())
#     sortedKeys.sort()
#
#
#     for movieKey in sortedKeys:
#         print(movieKey, "stars", films[movieKey])
#
# main()
#


def main():
    personalInfo = {"name":"kim"}

    # person wants multiple hobbies -> make that key map to a list
    personalInfo["hobbies"] = ["backpacking"]
    personalInfo["hobbies"].append("scuba diving")

    for key in personalInfo:
        print(key,personalInfo[key])


main()