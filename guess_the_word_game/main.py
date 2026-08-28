import random
#importing the random module to select a random word from the list of words

words = ("python", "programming", "computer", "algorithm", "function", "variable",
          "loop", "condition", "syntax", "debugging", "apple", "bridge", "cloud", 
          "dance", "eagle", "forest", "grape", "house", "island", "jungle", "kite", 
          "lemon", "mountain", "night", "ocean", "pencil", "queen", "river", "star", 
          "train", "umbrella", "velvet", "wind", "xylophone", "yellow", "zebra", "anchor", 
          "bucket", "candle", "door", "engine", "feather", "guitar", "hammer", "ink", 
            "jacket", "key", "ladder", "mirror", "net", "onion", "pillow", "quilt", "ring", 
            "soap", "telescope", "urn", "vase", "watch", "yarn")
#list of words to choose from for the game

print("Welcome to the Guess the Word Game!")
#welcome message for the game

word = random.choice(words)
#choosing a random word from the list of words

name = input("Enter your name: ")
#input for the player's name

m = ""
#initializing an empty string to store the letters guessed by the player

i = 0
while i < len(word) + 1:
    guess = input("guess the letter: ").lower()
    # getting the player's guess and converting it to lowercase for perfect matching 
    # with the word

    if guess in word:
        print("Correct guess! This letter is in the word.")
        m += guess
        #adding the guessed letter to the string of guessed letters

        print(f"Letters guessed so far: {m}")
        #printing the letters guessed so far by the player

    else:
        print("Incorrect guess.This letter is not in the word.")
    i += 1
if m == word:
    print(f"Congratulations, {name}! You've guessed the word '{word}' correctly!")
    #will print a congratulatory message if the player guesses the word correctly

else:
    print(f"Sorry, {name}. You failed to guess the word '{word}'.")
    #will print a message if the player fails to guess the word correctly

print("Thank you for playing the Guess the Word Game!")
#printing a thank you message for playing the game

print("Game developed by: Harshit")
#game developer's name