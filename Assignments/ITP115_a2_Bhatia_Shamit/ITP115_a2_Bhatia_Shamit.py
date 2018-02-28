# Shamit Bhatia
# ITP 115, Fall 2016
# Assignment 2
# Shamitbh@usc.edu

# Part 1:
# Harry Potter Vending Machine Program

knut = 1
sickle = 29
galleon = 493 #Setting variable values all in terms of knuts

butterBeer = 58
quill = 10
dailyProphet = 7
bookSpells = 400

change = 0
stringChange = "" #used later to concatenate strings
changeSickle = 0
changeKnut = 0

print("\nPlease select an item from the Vending machine: ")
userChoice = input("\na) Butterbeer: 58 Knuts\nb) Quill: 10 Knuts\nc) The Daily Prophet: 7 Knuts\nd) Book of Spells: 400 Knuts\n")

#print(userChoice)

if (userChoice.lower() == "a"):
    shareInsta = input("Are you willing to share your purchase on Instagram? You will receive a 5 Knut discount if you do! (y/n): ")
    if (shareInsta.lower() == "y"):
        butterBeer = 53
        change = galleon - butterBeer
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle #int division to cut off decimals
        print("\nYou bought a butterBeer for", butterBeer, "Knuts (with a coupon of 5 Knuts) and paid with one galleon.\n")
        print("Here is your change ("+stringChange+" Knuts):")
        print("Sickles:",changeSickle)
        print("Knuts:",changeKnut)
    elif (shareInsta.lower() != "n"):
        print("You have entered an invalid option. No coupon will be used.")
        change = galleon - butterBeer
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle
        print("\nYou bought a butterBeer for", butterBeer, "Knuts and paid with one galleon.\n")
        print("Here is your change ("+stringChange+" Knuts):")
        print("Sickles:",changeSickle)
        print("Knuts:",changeKnut)
    else:
        change = galleon - butterBeer
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle
        print("\nYou bought a butterBeer for", butterBeer, "Knuts and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)

elif (userChoice.lower() == "b"):
    shareInsta = input("Are you willing to share your purchase on Instagram? You will receive a 5 Knut discount if you do! (y/n): ") #see if shared on instagram
    if (shareInsta.lower() == "y"):
        quill = 5
        change = galleon - quill
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle  # int division to cut off decimals
        print("\nYou bought a Quill for", quill, "Knuts (with a coupon of 5 Knuts) and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)
    elif (shareInsta.lower() != "n"):
        print("You have entered an invalid option. No coupon will be used.")
        change = galleon - quill
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle  # int division to cut off decimals
        print("\nYou bought a Quill for", quill, "Knuts and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)
    else:
        change = galleon - quill
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle  # int division to cut off decimals
        print("\nYou bought a Quill for", quill, "Knuts and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)

elif (userChoice.lower() == "c"):
    shareInsta = input("Are you willing to share your purchase on Instagram? You will receive a 5 Knut discount if you do! (y/n): ")
    if (shareInsta.lower() == "y"):
        dailyProphet = 2
        change = galleon - dailyProphet
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle  # int division to cut off decimals
        print("\nYou bought The Daily Prophet for", dailyProphet, "Knuts (with a coupon of 5 Knuts) and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)
    elif (shareInsta.lower() != "n"):
        print("You have entered an invalid option. No coupon will be used.")
        change = galleon - dailyProphet
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle  # int division to cut off decimals
        print("\nYou bought The Daily Prophet for", dailyProphet, "Knuts and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)
    else:
        change = galleon - dailyProphet
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle  # int division to cut off decimals
        print("\nYou bought The Daily Prophet for", dailyProphet, "Knuts and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)

elif (userChoice.lower() == "d"):
    print("d")
    shareInsta = input("Are you willing to share your purchase on Instagram? You will receive a 5 Knut discount if you do! (y/n): ")

    if (shareInsta.lower() == "y"):
        bookSpells = 395
        change = galleon - bookSpells
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle  # int division to cut off decimals
        print("\nYou bought a Book of Spells for", bookSpells, "Knuts (with a coupon of 5 Knuts) and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)
    elif (shareInsta.lower() != "n"):
        print("You have entered an invalid option. No coupon will be used.")
        change = galleon - bookSpells
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle  # int division to cut off decimals
        print("\nYou bought a Book of Spells for", bookSpells, "Knuts and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)
    else:
        change = galleon - bookSpells
        stringChange = str(change)
        changeKnut = change % sickle
        changeSickle = change // sickle  # int division to cut off decimals
        print("\nYou bought a Book of Spells for", bookSpells, "Knuts and paid with one galleon.\n")
        print("Here is your change (" + stringChange + " Knuts):")
        print("Sickles:", changeSickle)
        print("Knuts:", changeKnut)

else:
    print("You have selected an invalid option. You will be given a Quill for 10 Knuts.")
    change = galleon - quill
    stringChange = str(change)
    changeKnut = change % sickle
    changeSickle = change // sickle  # int division to cut off decimals
    print("\nYou bought a Quill for", quill, "Knuts and paid with one galleon.\n")
    print("Here is your change (" + stringChange + " Knuts):")
    print("Sickles:", changeSickle)
    print("Knuts:", changeKnut)


# Part 2:
# Choose Your own Adventure Game Program

print("\n\n\nWelcome to the Choose your own adventure game!\n")

print("It's your first day of school at USC! You're excited, but nervous. "
      "Looking at your schedule, you realize you have a few hours to kill before your next class."
      "\nYou haven't really explored campus much and would love to explore more. So you pull out your phone and look at the \"USC MAPS\" app."
      "\nThe top three attractions you remember from orientation are within walking distance.\n\nDo you:")
choiceLoc = input("a) Go to the Bookstore\nb) Go to the EVK Dining hall\nc) Go to the Lyon Center\n")
if (choiceLoc.lower() == "a"): #choiceLoc for location choice at beginning
    print("\nYou walk inside the Bookstore and everything looks extremely new and renovated. \nYou think to yourself, "
          "'Wow! this place is like a candy shop for students. There's even actual candy in here!'\nYou decide to check out the different floors."
          "\n\nWhich floor should you go to?\n")
    choiceFloor = input("a) First Floor (Game day items)\nb) Second Floor (Clothing)\nc) Basement (Textbooks)\n")
    if (choiceFloor.lower() == "a"):
        print("You check out all the USC game day gear and end up buying a beautiful \"Fight On\" hat."
              "\nIt looks gorgeous and you're now ready for class.")
    elif (choiceFloor.lower() == "b"):
        print("You go upstairs to the Second Floor and find a great sweatshirt that's super versatile for any occasion!"
              "\nYou're ready to tackle your next class.")
    elif (choiceFloor.lower() == "c"):
        print("You go downstairs and luckily remember you need to buy a textbook for your next class."
              "\nYou're overwhelmed by the price but purchase it anyway. Now you're truly ready for syllabus week.")
    else:
        print("You entered an invalid choice and have decided to check out the Basement.\n")
        print("You go downstairs and luckily remember you need to buy a textbook for your next class."
              "\nYou're overwhelmed by the price but purchase it anyway. Now you're truly ready for syllabus week.")
elif (choiceLoc.lower() == "b"):
    print("\nYou find yourself entering the EVK dining hall as your stomach starts to grumble. "
          "\n'Good timing', you say to your stomach under your breath.")
    print("\n\nWhat would you like to eat?")
    choiceEat = input("a) Eggs\nb) Cereal\n")
    if (choiceEat.lower() == "a"):
        print("You go get some hard-boiled eggs to peel and eat 2 of them, before feeling full."
              "\nNow that your stomach's happy, you're ready to learn in class!")
    elif (choiceEat.lower() == "b"):
        print("You get a bowl of your favorite cereal, \"Lucky Charms.\" "
              "It reminds you of how lucky you are to be attending such a great college like USC.\n"
              "You get extremely excited about finishing off your first day at such a beautiful school!")
    else:
        print("You entered an invalid choice and went with your instinct to go get cereal.\n")
        print("You get a bowl of your favorite cereal, \"Lucky Charms.\" "
              "It reminds you of how lucky you are to be attending such a great college like USC.\n"
              "You get extremely excited about finishing off your first day at such a beautiful school!")
elif (choiceLoc.lower() == "c"):
    print("You enter the Lyon Center and the first thing you notice is how many good-looking people there are, working out.")
    print("Thank goodness you remembered to pack gym clothes in your bag today.")
    print("\n\nDo you want to:")
    choiceWorkout = input("a) Do some cardio\nb) Lift some weights\n")
    if (choiceWorkout.lower() == "a"):
        print("You go upstairs and hop on the treadmill for 30 minutes. It feels good to run after a while."
              "\nYou now feel energized for class and ready to take on the day!")
    elif (choiceWorkout.lower() == "b"):
        print("You go to the weight room and do an intense arm-day session. It feels good to workout after a while."
              "\nYou now feel energized for class and ready to take on the day!")
    else:
        print("You entered an invalid choice and ended up craving some cardio.\n")
        print("You go upstairs and hop on the treadmill for 30 minutes. It feels good to run after a while."
              "\nYou now feel energized for class and ready to take on the day!")
else: #any choice other than a, b, or c becomes a
    print("You entered an invalid choice and have decided to go to the nearest location (The EVK Dining Hall):\n")
    print("\nYou find yourself entering the EVK dining hall as your stomach starts to grumble. "
          "\n'Good timing', you say to your stomach under your breath.")
    print("\n\nWhat would you like to eat?\n")
    choiceEat = input("a) Eggs\nb) Cereal\n")
    if (choiceEat.lower() == "a"):
        print("You go get some hard-boiled eggs to peel and eat 2 of them, before feeling full."
              "\nNow that your stomach's happy, you're ready to learn in class!")
    elif (choiceEat.lower() == "b"):
        print("You get a bowl of your favorite cereal, \"Lucky Charms.\" "
              "It reminds you of how lucky you are to be attending such a great college like USC.\n"
              "You get extremely excited about finishing off your first day at such a beautiful school!")
    else:
        print("You entered an invalid choice and went with your instinct to go get cereal.\n")
        print("You get a bowl of your favorite cereal, \"Lucky Charms.\" "
              "It reminds you of how lucky you are to be attending such a great college like USC.\n"
              "You get extremely excited about finishing off your first day at such a beautiful school!")


print("\n\nTHE END!") #ends adventure game with sign-off