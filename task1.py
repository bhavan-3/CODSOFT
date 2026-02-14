def to_do_list():
    tasks = []

    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added")

        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed")
            else:
                print("Task not found")

        elif choice == "3":
            print("Tasks:")
            if not tasks:
                print("No tasks available")
            else:
                for task in tasks:
                    print("- " + task)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


to_do_list()
