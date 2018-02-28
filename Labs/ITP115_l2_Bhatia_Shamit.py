# Shamit Bhatia
# ITP 115, Fall 2016
# Lab L2
# Shamitbh@usc.edu

# import random

sizeCoffee = input("What size coffee do you want(S, M, L): ")
if (sizeCoffee.lower() == "s"):
    sizeCoffee = "small"
elif (sizeCoffee.lower() == "m"):
    sizeCoffee = "medium"
elif (sizeCoffee.lower() == "l"):
    sizeCoffee = "large"
else: #user enters a letter that is not s, m, or l
    print("Please follow the directions.")

wordTempCoffee = "" #if user enters temp > 150, "hot", if temp < 150, "cold" -> variable stores the user's temp (int) as a string (hot or cold)

tempCoffee = int(input("What temperature would you like(in degrees Fahrenheit)?: "))
if (tempCoffee > 150):
    wordTempCoffee = "hot"
elif (tempCoffee > 0):
    wordTempCoffee = "cold"
else: #user enters a negative temp.
    print("Please follow the directions.")

beansType = input("What type of beans / blend would you like?: ")
if beansType == "":
    print ("Please follow directions")

roomCream = input("Would you like room for cream (y/n)?: ")
if (roomCream.lower() == "y"):
    roomCream = "Cream"
elif (roomCream.lower() == "n"):
    roomCream = "No Cream"
else: #user enters a letter that's not y or n
    print("Please follow the directions.")

print("\n")
print("You ordered a",sizeCoffee, wordTempCoffee, beansType,"with",roomCream)


# randomDrink = input("Would u also like me to generate a random temp bro? (y/n)")
# if (randomDrink.lower() == "y"):
#     print("Sweet. ", end="")
#     tempRand = random.randrange(100, 180)
#     print("Your temp. is:",tempRand)
# else:
#     print("Aight bro no worries.")
