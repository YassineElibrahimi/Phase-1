# Mark tasks complete/incomplete
# Priority levels (High/Medium/Low)
# Due dates with datetime validation
# File persistence (save/load to JSON)
# Search by priority or status







import json



def menu():
    print("1. Add Task")
    print("2. remove task")
    print("3. Display Task")
    print("4. Mark Task as complete/incomplete")
    print("5.Search by priority or status")
    print("6. Exit")


def pause():
    input("\nPress Enter to continue")


def priorities():
    print("Add priority:\n1.High\n2.Med\n3.Low")
    try:
        choice_priority = int(input("Add operation: "))
    except ValueError:
        print("Invalid,Please enter a number")
    priority_list = ["High","Med","Low"]
    priority = priority_list[choice_priority - 1]
    return priority


# PS : I can change this def name to be add_note()/add_comment, and make a validate dead_line() function
def dead_line():
    while True:
        choice_deadline = input("Add deadline (Y/N): ").upper()

        if choice_deadline == "Y":
            date = input("add deadline: ")
            deadline =date
            return deadline
        elif choice_deadline == "N":
            deadline = None
            return deadline


def add_task(task,priority,deadline,status):
    return {"task":task,"priority":priority,"deadline":deadline,"status":status}


def show_tasklist(tasklist):
    for i, task in enumerate(tasklist,start= 1):
        print(f"{i} - {task}")


def complete(tasklist,choice_complete):
    if tasklist[choice_complete - 1]["status"]:
        print("The task already mark as complete")

    else:
        tasklist[choice_complete - 1]["status"] = True
        print("The task is marked as complete")


def incomplete(tasklist,choice_incomplete):
    if not tasklist[choice_incomplete - 1]["status"]:
        print("The task already mark as incomplete")

    else:
        tasklist[choice_incomplete - 1]["status"] = False
        print("The task is marked as incomplete")


def main():
    try:
        with open("task-manager.json", "r") as f:
            tasklist = json.load(f)
    except FileNotFoundError:
        tasklist = []

    while True:
        menu()
        try:
            user = int(input("Choose an operation: "))
        except ValueError:
            print("Invalid,Please enter a number")

# __________________________ ADD TASKS __________________________

        if user == 1:
        # collect inputs and send them yo add_task()
            task = input("Add Task: ")
            priority = priorities()
            deadline = dead_line()

        # add task to list:
            task_info = add_task(task, priority, deadline, status=False)
            tasklist.append(task_info)
            print("The task is added successfully")
            pause()

# __________________________ REMOVE TASKS __________________________

        elif user == 2:
            show_tasklist(tasklist)

            try:
                to_remove = int(input("task number"))
                tasklist.pop(to_remove - 1)
                print("The task is removed successfully")
            except ValueError:
                print("Invalid,Please enter a number")

            pause()

# __________________________ DISPLAY TASKS __________________________

        elif user == 3:
            show_tasklist(tasklist)
            pause()

# ________________________ COMPLETE/INCOMPLETE ______________________

        elif user == 4:
            show_tasklist(tasklist)

            print("Mark the task as\n1.Complete\n2.Incomplete")
            try:
                choice = int(input("Enter operation."))
            except (ValueError, IndexError):
                print("Invalid,Please enter operator Number")

            if choice == 1:
                try:
                    choice_complete = int(input("Enter the task number to mark as complete:"))
                    complete(tasklist, choice_complete)
                except (ValueError, IndexError):
                    print("Invalid,Please enter task number")

                pause()

            elif choice == 2:
                try:
                    choice_incomplete = int(input("Enter the task number to mark as incomplete:"))
                    incomplete(tasklist, choice_incomplete)
                except (ValueError, IndexError):
                    print("Invalid,Please enter task number")

                pause()


        # _____________________ SEARCH BY PRIORITY/DEADLINE ________________________

        elif user == 5:
            print("1. Search by priority\n2. Status")
            choice = int(input("choose an  operation:"))

            if choice == 1:
                sorted_tasklist = sorted(tasklist, key=lambda d: d["priority"])
                print(sorted_tasklist)

            elif user == 2:
                sorted_tasklist = sorted(tasklist, key=lambda d: d["status"])
                print(sorted_tasklist)

# ____________________ File persistence (save/load to JSON) __________________________

        elif user == 6:
            with open("task-manager.json","w") as f:
                json.dump(tasklist, f, indent= 2)
            print("Program Exit")
            break


main()






