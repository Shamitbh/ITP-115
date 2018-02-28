# Shamit Bhatia
# ITP 115, Fall 2016
# Assignment 7
# Shamitbh@usc.edu
# Purpose: Create a program simulating a user's music library with Dictionaries.

import pickle
import random

def main():

    # loadlibrary
    musicDCT = loadLibrary("music_library.dat")

    # loop through menu
    loopControl = True

    while (loopControl):
        displayMenu()
        choice = input("> ")
        if (choice == "7"):
            break
        elif (choice != "1" and choice!= "2" and choice!= "3" and choice!= "4" and choice!= "5" and choice!= "6" and choice != "8"):
            print("Invalid entry!")
            continue
        elif (choice == "1"):
            # display library
            displayLibrary(musicDCT)
        elif (choice == "2"):
            # Display all artists
            displayArtists(musicDCT)
        elif (choice == "3"):
            # add album
            addAlbum(musicDCT)
        elif (choice == "4"):
            # delete album
            albumDel = deleteAlbum(musicDCT)
            if albumDel == True:
                print("Delete album success!")
            else:
                print("Delete album failed.")
        elif (choice == "5"):
            # delete artist
            artistDel = deleteArtist(musicDCT)
            if artistDel == True:
                print("Delete artist success!")
            else:
                print("Delete album failed.")
        elif (choice == "6"):
            # search library
            searchLibrary(musicDCT)
        # EXTRA CREDIT
        else:
            print("Generating random playlist...")
            generateRandomPlaylist(musicDCT)

    saveLibrary("music_library.dat",musicDCT)
    print("Data saved to file 'music_library.dat'")
    print("\nHave a great day!")

def displayMenu():
    # print entire menu
    print("\nWelcome to Your Music Library")
    print("Options:")
    print("\t1) Display library")
    print("\t2) Display all artists")
    print("\t3) Add an album")
    print("\t4) Delete an album")
    print("\t5) Delete an artist")
    print("\t6) Search library")
    print("\t7) Exit")
    print("\t8) Generate Random Playlist")


def loadLibrary(libraryFileName):

    fileIn = open(libraryFileName,"rb")

    # use pickle.load()
    musicDict = pickle.load(fileIn)

    # Close file
    fileIn.close()

    # return dictionary representing music lib.
    return musicDict

def saveLibrary(libraryFileName, musicLibDct):

    fileOut = open(libraryFileName,"wb")

    # use pickle.dump()
    pickle.dump(musicLibDct, fileOut)

    # Close file
    fileOut.close()

def displayLibrary(musicLibDct):

    # print out entire music library
    for key in musicLibDct:
        print("Artist:", key)
        print("Albums:")
        for album in musicLibDct[key]:
            print("\t-",album)
        print()


def displayArtists(musicLibDct):

    # print out all artists currently in user's music library
    print("Displaying all artists:")
    for key in musicLibDct:
        print("-",key)

def addAlbum(musicLibDct):

    # ask user for name of artist AND name of album they want to add
    bandName = input("Enter band: ")
    bandName = bandName.title()

    albumName = input("Enter album: ")
    albumName = albumName.title()

    # check if artist already in dict.

    # if so, add album to artists existing list
    if bandName in musicLibDct:
        musicLibDct[bandName].append(albumName)
    # if not, add a new key (artist) to dict. and the new value [list (name of album)]
    else:
        musicLibDct[bandName] = [albumName]

def deleteAlbum(musicLibDct):


    # Ask user for name of artist and name of album to remove
    artist = input("Enter artist: ")
    artist = artist.title()
    album = input("Enter album: ")
    album = album.title()

    # Check that BOTH artist AND album are in dictionary before removing
    for key in musicLibDct:
        if key == artist:
            if album in musicLibDct[key]:
                musicLibDct[artist].remove(album)
                return True
    return False

def deleteArtist(musicLibDct):

    # Ask user for name of artist
    # Check if artist in dict. before deleting artist

    artist = input("Enter artist:")
    artist = artist.title()

    if artist in musicLibDct:
        del musicLibDct[artist]
        return True
    else:
        return False

def searchLibrary(musicLibDct):

    # ask user for a search term (either artist or album)
    # Search should NOT be case sensitive
    searchTerm = input("Please enter a search term: ")
    searchTermLower = searchTerm.lower()

    # artist
    # print out any artists containing search term
    counter1 = 0 # keep track of if any results
    print("Artists containing"+"'"+searchTerm+"'")
    for key in musicLibDct:
        if searchTermLower in key.lower():
            print("-",key)
            counter1 += 1
        else:
            continue
    if counter1 == 0:
        print("\tNo results")
    # print out any albums containing search term

    counter2 = 0
    print("Albums containing"+"'"+searchTerm+"'")
    for key in musicLibDct.values():
        for album in key:
            if searchTermLower in album.lower():
                print("-",album)
                counter2 += 1
            else:
                continue
    if counter2 == 0:
        print("\tNo results")

def generateRandomPlaylist(musicLibDct):
    print("\nAlbum : Artist")
    print("--------------")
    for key in musicLibDct:
        print(random.choice(musicLibDct[key]),":",key)


main()