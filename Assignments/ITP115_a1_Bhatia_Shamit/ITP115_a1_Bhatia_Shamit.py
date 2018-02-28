"""
Shamit Bhatia
ITP 115
Assignment 1
9/1/2016

Description:
This program creates a Mad Libs Story
"""

animalPlural = input("Enter an animal (plural): ")#
adjectiveOne = input("Enter an adjective (emotion): ")#
adjectiveTwo = input("Enter another adjective (color): ")#
verb = input("Enter a present-tense verb ending in -ing: ")#
nameMale = input("Enter a male character's name: ") #
num1 = int(input("Enter a number greater than 1: "))#
num2 = int(input("Enter a second number: "))#
num3 = int(input("Enter a third number: "))#
num4 = float(input("Enter a number with a decimal less than 5 but greater than 1: "))#number w/ decimal
num5 = num2+num3 #

print("\nToday I went to the Zoo with",nameMale,"and we saw",num1,adjectiveOne,animalPlural+". \nThey are really good at",verb+".",nameMale,"has been to the Zoo",num2,"times and I have been",num3,"times.\nIn total, we've been to the Zoo",num5,"times.\nWhile walking around, we saw so many",adjectiveTwo,"flags. We ended up walking around the Zoo today for",num4,"hours! What a fun but exhausting day!")
