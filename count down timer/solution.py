import time
print("Welcome to countdown timer")
duration = int(input("Enter the duration of the timer in seconds: "))
while duration > 0:
    print(f"Time remaining: {duration} seconds", end="\r")
    time.sleep(1)
    duration -= 1
print("Time's up!")