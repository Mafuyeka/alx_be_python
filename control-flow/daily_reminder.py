def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task"
        case _:
            reminder = f"Reminder: '{task}' has an unknown priority level"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no" and priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."

    print(reminder)  # ✅ Starts with "Reminder:" in all cases

if __name__ == "__main__":
    main()
