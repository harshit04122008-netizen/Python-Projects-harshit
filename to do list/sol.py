import time 

task_list = []

choice = "y"

while choice.lower() == "y":
    task = input("Enter a task: ")
    due_date = input("Enter the due date for this task (YYYY-MM-DD): ")
    due_time = input("Enter the due time for this task (HH:MM): ")
    task_list.append([task, due_date, due_time])
    choice = input("Do you want to add another task? (y/n): ")


print("Your to-do list:")

for task in task_list:
    print(f"- {task}")

print("Your to-do list has been saved.")

time.sleep(2)  # Simulate saving time

choice = input("wanna remove a task? (y/n): ")

if choice.lower() == "y":
    task_to_remove = input("Enter the task you want to remove: ")

    if task_to_remove in task_list:
        task_list.remove(task_to_remove)
        print(f"Task '{task_to_remove}' has been removed.")

    else:
        print(f"Task '{task_to_remove}' not found in the list.")
