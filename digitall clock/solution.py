from random import choice
import time
print("Digital Clock")
choice = input("Do you want to see the time in 12-hour format or 24-hour format? (Enter 12 or 24): ")
stop = False
while not stop:
    if choice == "12":
        print(time.strftime("%I:%M:%S %p"))
    else:
        print(time.strftime("%H:%M:%S"))
    st = input("Press 'q' to quit or any other key to continue: ")
    if st == "q":
        stop = True
        
