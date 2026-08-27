import random
#importing the file random to generate a random number

n = int(input("Enter the number of attempts you want: "))
#getting the number of attempts from the user

r = int(input("Enter the range of numbers (1 to n): "))
#getting the range of numbers from the user

number = random.randint(1, r)
#randomly generating a number between 1 and the user-defined range

guess = None
#intializing the guess variable to None

i = 0

while i < n:

    guess = int(input(f"Guess a number between 1 and {r}: "))

    if guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print("Congratulations! You guessed the number.")
        break

    if i == n:
        print(f"Sorry, you've used all your attempts. The number was {number}.")
        break

    i += 1
print("Game Over!")
print("Thank you for playing!")