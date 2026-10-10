import time 

task_list = []

choice = "y"

def remove_task(task_list, task_to_remove):
    for task in task_list:
        if task[0] == task_to_remove:
            task_list.remove(task)
            print(f"Task '{task_to_remove}' has been removed from the list.")
            return
        else:
            print(f"Task '{task_to_remove}' not found in the list.")
            return

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


for i in range(len(task_list)):
    print(f"{i + 1}. {task_list[i][0]} - Due: {task_list[i][1]} at {task_list[i][2]}")  
    if due_date < time.strftime("%Y-%m-%d") or (due_date == time.strftime("%Y-%m-%d") and due_time < time.strftime("%H:%M")):
        print("   This task is overdue!")

completed = input("Have you completed any tasks? (y/n): ")
if completed.lower() == "y":
    task_to_remove = input("Enter the task you have completed: ")
    remove_task(task_list, task_to_remove)


choice = input("Do you want to view your tasks? (y/n): ")

if choice.lower() == "y":
    if len(task_list) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your current to-do list:")
        for i in range(len(task_list)):
            print(f"{i + 1}. {task_list[i][0]} - Due: {task_list[i][1]} at {task_list[i][2]}")
            task_to_remove = input("Enter the task you have to remove: ")
            remove_task(task_list, task_to_remove)

if len(task_list) == 0:
    print("Your to-do list is empty.")
else:
    print("Your final to-do list:")
    for i in range(len(task_list)):
        print(f"{i + 1}. {task_list[i][0]} - Due: {task_list[i][1]} at {task_list[i][2]}")
