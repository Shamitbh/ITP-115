from Superhero import Superhero


def main():

    while (True):
        # Get user input for object parameters

        # fighter 1 stats
        name1 = input("\nEnter fighter #1's name:\n")
        type1 = input("Is fighter #1 a hero or a villain?:\n")

        # EXTRA CREDIT
        while type1.lower() != "hero" and type1.lower() != "villain":
            print("Invalid input! Please enter a proper selection.")
            type1 = input("Is fighter #1 a hero or a villain?:\n")

        attack1 = input("Enter fighter #1's attack points:\n")

        # fighter 2 stats
        name2 = input("\nEnter fighter #2's name:\n")
        type2 = input("Is fighter #1 a hero or a villain?:\n")

        # EXTRA CREDIT
        while type2.lower() != "hero" and type2.lower() != "villain":
            print("Invalid input! Please enter a proper selection.")
            type2 = input("Is fighter #2 a hero or a villain?:\n")

        attack2 = input("Enter fighter #2's attack points:\n")

        # Create 2 player objects
        player1 = Superhero(name1, type1, attack1)
        player2 = Superhero(name2, type2, attack2)


        print("\nFIGHTERS\n")
        print(player1)
        print(player2)
        print("\nBEGINNING BATTLE!\n")

        # Counter - keep track of which round it is
        counter = 1

        while (not player1.isDead() and not player2.isDead()):
            print("====== ROUND",counter,"======")
            player1.loseHealth(player2.getAttack())
            player2.loseHealth(player1.getAttack())

            print(player1)
            print(player2)
            print()

            counter += 1

        if player1.isDead() and player2.isDead():
            print("The fight resulted in a Tie!")
        elif player1.isDead():
            print(player2.getName(),"won!")
        else:
            print(player1.getName(),"won!")

        # control loop to play again
        userContinue = input("\nWould you like to play again? (y/n): ")
        while userContinue.lower() != "n" and userContinue.lower() != "y":
            print("Please enter a valid selection.")
            userContinue = input("Would you like to play again? (y/n): ")
        if userContinue.lower() == "y":
            continue
        else:
            break
    print("Goodbye!")
main()