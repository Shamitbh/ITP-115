# Lists and tuples

genres = ["crunk", "alternative", "jazz", "rap"]

for genre in genres:
    print(genre, end=" ")

genres.append("hip hop")

for item in genres: # iterate through each genre
    for letter in item: # iterate through each letter in given genre
        if letter not in "aeiou":
            # Print all non-vowel letters
            print(letter, end="")
    print()
