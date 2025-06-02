def main():
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process task using if-elif-else (instead of match-case)
    if priority == "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to get it done as soon as possible.")
    elif priority == "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to do it soon.")
    elif priority == "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that still requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    else:
        print("Invalid priority. Please enter high, medium, or low.")

# Loop to allow multiple tasks if you want
while True:
    main()
    repeat = input("\nDo you want to enter another task? (yes/no): ").lower()
    if repeat != "yes":
        print("Goodbye! Stay productive.")
        break
