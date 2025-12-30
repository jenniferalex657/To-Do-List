# Simple To-Do List (10 items)

tasks = [
    "Buy groceries",
    "Read a book",
    "Go for a walk",
    "Clean the room",
    "Pay bills",
    "Call a friend",
    "Finish homework",
    "Exercise",
    "Cook dinner",
    "Plan the week"
]

done = [False] * len(tasks)

while True:
    # Show tasks
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        mark = "x" if done[i-1] else " "
        print(f"{i}. [{mark}] {task}")

    # Ask which task to toggle
    choice = input("\nEnter task number to toggle (or 'q' to quit): ")
    if choice.lower() == 'q':
        print("Bye!")
        break
    if choice.isdigit():
        num = int(choice)
        if 1 <= num <= len(tasks):
            done[num-1] = not done[num-1]
        else:
            print("Invalid task number!")
    else:
        print("Please enter a number or 'q' to quit.")