# Shamit Bhatia
# ITP 115, Fall 2016
# Lab L3
# Shamitbh@usc.edu

i = 10
numSymbols = 1
numSpace = 18

while (i > 0):
    print(numSpace*" "+" ^"*numSymbols+"\n")
    numSpace = numSpace - 2
    numSymbols = numSymbols + 2
    i = i - 1