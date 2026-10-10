import random

n = int(input("Enter the length of the password: "))

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-+"

all_characters = lower + upper + numbers + symbols

print(f"Generated password: {''.join(random.choice(all_characters) for _ in range(n))}")