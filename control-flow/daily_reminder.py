task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder = ""

if priority.lower() == "high":
    reminder = f"Reminder: '{task}' is a high priority task"
elif priority.lower() == "medium":
    reminder = f"Note: '{task}' is a medium priority task"
elif priority.lower() == "low":
    reminder = f"Note: '{task}' is a low priority task"
else:
    reminder = f"Note: '{task}' has an unrecognized priority level"

if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)
