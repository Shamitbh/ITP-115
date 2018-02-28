## FUNCTIONS ##

# Define function (recipe for coffee)
    # def functionName ():
#         statements(s)
# Eg.
# def spam ():
#     print("spam, spam, spam")
#

# Call function (looks at recipe and actually makes coffee)
    # functionName ()
# Eg.
# spam ()
# spam ()
#
# import random
# #healthTip will generate a random health tip for you.
# def healthTip():
#     num = random.randrange(3) # generates a random number from 0-3 not including 3 so 0, 1, or 2
#     if num == 0:
#         print("Floss daily.")
#     elif num == 1:
#         print("Drink 8 glasses of water per day.")
#     elif num == 2:
#         print("An apple a day keeps the doctor away.")
#     else:
#         print("Error: this should never happen.")
#
# for i in range(10):
#     healthTip()
#
# # Function using parameters
# def display (message):
#     print(message)
#
# display("Hi Mom")


####################################


# def inspirationQuote(day):
#     if day.lower() == "monday":
#         print("Limitless possibilities!")
#     elif day.lower() == "tuesday" or day.lower() == "wednesday" or day.lower() == "thursday":
#         print("Hang in there!")
#     elif day.lower() == "friday" or day.lower() == "saturday" or day.lower() == "sunday":
#         print("YAY ITS THE WEEKEND!")
#     else:
#         print("Hmm, I don't know that day")
#
# #### NOTE: Anything created in a function dies in the function at the end ####
#
# # ------------
#
# dayOfTheWeek = input("What day is it?")
#
# inspirationQuote(dayOfTheWeek)

################################################

# # Using default parameter values
# def birthday(name = "Cooper", age = 1):
#     print("Happy birthday "+name+". You are now "+str(age))
#
# #when calling, use default parameter values if no other parameters are entered
# birthday()

#################################################

# Return values (Function output)

# def chemicalGroup(chemical):
#     group = ""
#     if chemical.lower() == "fluorine":
#         group = "halogen"
#     elif chemical.lower() == "sodium":
#         group = "alkaline"
#     elif chemical.lower() == "iron":
#         group = "transition metal"
#     else:
#         group = "unknown"
#     return group
# #------------------------------
#
# chem = input("Hey chemical fan! Please give me an element: ")
# groupName = chemicalGroup(chem) # must store it in something if theres a return value
#
# print("The element", chem ,"is in the group", groupName)

###################################################

def sumSomeNumbers(numberList):
    total = 0
    for num in numberList:
        total += num
        # print(num)
    return total


numbers = [8, 5, 90, 107, 45]

print("The sum of", numbers ,"is", sumSomeNumbers(numbers))