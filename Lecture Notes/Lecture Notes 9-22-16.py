# Functions, continued

# Scope (if a variable is in a function, its local to only that function

# Constants are ALL_CAPS_WITH_UNDERSCORES
# Global constants are created in global namespace
    # They are defined on left side (not in functions)
    # Will not change value once they are assigned

# Main() function is often starting point of actual program.. Then you basically call other functions in the main
    # From now on, ONLY USE MAIN in your python assignments
    # At the end of each assignment, ALWAYS CALL MAIN with main()


def sumSomeNumbers(numberList):
    total = 0
    for num in numberList:
        total += num
        # print(num)
    return total


def main():
    numbers = [8, 5, 90, 107, 45]
    print("The sum of", numbers ,"is", sumSomeNumbers(numbers))

main()

# The only things on the far left of my file should be:
    # def function:
    # CREATING CONSTANTS
    # # Coments
    # import something
    # main()