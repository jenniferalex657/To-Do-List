tasks = []
done = []

print("Enter your tasks.")
print("Type 'done' when finished adding tasks.\n")

while True:
    task = input("Add task: ")
    if task.lower() == "done":
        break
    tasks.append(task)
    done.append(False)

while True:
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        mark = "x" if done[i - 1] else " "
        print(f"{i}. [{mark}] {task}")

    choice = input("\nEnter task number to toggle (or 'q' to quit): ")

    if choice.lower() == "q":
        print("Goodbye!")
        break
    elif choice.isdigit():
        num = int(choice)
        if 1 <= num <= len(tasks):
            done[num - 1] = not done[num - 1]
        else:
            print("Invalid task number.")
    else:
        print("Please enter a number or 'q'.")