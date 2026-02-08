# Task : Code Review: Refactor Day 6 Task Manager - fix any lingering issues, improve UX
import json
from datetime import datetime



PRIORITY_ORDER = {"High":1, "Med":2 ,"Low":3 }
priority_list = ["High", "Med", "Low"]




def main():
    tasklist = load_tasks()

    while True:
        menu()
        try:
            user = int(input("Choose an operation: "))
        except ValueError:
            print("Invalid,Enter a number")
            continue

    # __________________________ ADD TASKS __________________________

        if user == 1:
        # collect inputs and send them to add_task()
            task = input("Add Task: ")
            if not task:
                print("Invalid, The task is Empty")
                continue

            priority = priorities()
            deadline = get_deadline()
            pause()
        # then add task to list:
            task_info = add_task(task, priority, deadline, status=False)
            tasklist.append(task_info)
            print("The task is added successfully")
            pause()


    # __________________________ REMOVE TASKS __________________________

        elif user == 2:
            show_tasklist(tasklist)

            try:
                to_remove = int(input("task number"))
                if not 1 <= to_remove <= len(tasklist):
                    print("Invalid task number")
                    continue
            except ValueError:
                print("Invalid,Enter a Number")
                continue
            tasklist.pop(to_remove - 1)
            print("The task is removed successfully")
            pause()


    # __________________________ DISPLAY TASKS __________________________

        elif user == 3:
            show_tasklist(tasklist)
            pause()

    # ________________________ COMPLETE/INCOMPLETE ______________________

        elif user == 4:
            show_tasklist(tasklist)

            print("Mark the task as:\n1.Complete\n2.Incomplete")
            try:
                choice = int(input("Enter operation."))
            except ValueError:
                print("Invalid,Enter a valid Number")
                continue


            if choice == 1:
                try:
                    choice = int(input("Enter the task number to mark as complete: "))
                    if not 1 <= choice <= len(tasklist):
                        print("Invalid task number")
                        continue

                except ValueError:
                    print("Invalid, Enter a Number")
                    continue
                complete(tasklist, choice)
                pause()

            elif choice == 2:
                try:
                    choice = int(input("Enter the task number to mark as incomplete:"))
                    if not 1 <= choice <= len(tasklist):
                        print("Invalid task number")
                        continue

                except ValueError:
                    print("Invalid,Please enter the task Number")
                    continue
                incomplete(tasklist, choice)
                pause()

            else:
                print("Invalid Choice")
                pause()
                continue


    # _____________________ SORT BY PRIORITY/DEADLINE ________________________

        elif user == 5:
            print("\n1.Sort by priority\n2.Sort by status")
            try:
                choice = int(input("choose an option:"))
            except ValueError:
                print("Invalid,Enter a Number")
                continue

            if choice == 1:
                sorted_tasklist = sorted(tasklist, key=lambda d: PRIORITY_ORDER[d["priority"].lower()])
                show_tasklist(sorted_tasklist)

            elif choice == 2:
                sorted_tasklist = sorted(tasklist, key=lambda d: d["status"])
                show_tasklist(sorted_tasklist)

            else :
                print("Invalid Choice")
                pause()
                continue
    
    # ____________________  SAVE and EXIT __________________________

        elif user == 6:
            save_tasks(tasklist)
            print("Program Exit, Goodbye 👋")
            break

        else:
            print("Invalid menu option.")



def menu():
    print("\n" + "-" * 40)
    print("============= Task Manager =============")
    print("-" * 40)
    print("1. Add Task")
    print("2. Remove task")
    print("3. Display Task")
    print("4. Mark Task as complete/incomplete")
    print("5. View sorted tasks")
    print("6. Exit")


def pause():
    input("\nPress Enter to continue")


def priorities():
    while True:
        print("Choose priority:")
        for i , priority in enumerate(priority_list, start= 1):
            print(f"{i} - {priority}")

        try:
            choice = int(input("Enter choice: "))
            if 0 < choice <= len(priority_list):
                return priority_list[choice - 1]

        except ValueError:
            print("Invalid,Enter a Number")
            continue

        else:
            print("Invalid, Enter a valid Number")


def get_deadline_date():
    while True:
        add_deadline = input("Add deadline (DD-MM-YYYY): ")
        try:
            deadline = datetime.strptime(add_deadline, "%d-%m-%Y")
            if deadline.date() < datetime.now().date():
                print("Invalid Date")
            else:
                print("Deadline added successfully")
                return deadline.strftime("%d-%m-%Y")
        except ValueError:
            print("Invalid format, Use DD-MM-YYYY")
            continue


def get_deadline():
    while True:
        choice = input("Add deadline? (Y/N): ").upper()

        if choice == "Y":
            return get_deadline_date()

        elif choice == "N":
            return None
        else:
            print("Invalid Choice")


def add_task(task,priority,deadline,status):
    return {"task":task,"priority":priority,"deadline":deadline,"status":status}


def show_tasklist(tasklist):
    if not tasklist:
        print("\nNo tasks available.")
        return


    print()
    for i, task in enumerate(tasklist, 1):
        status = "Done" if task["status"] else "Pending"
        deadline = task["deadline"] if task["deadline"] else "No deadline"
        print(f"{i}. {task['task']}")
        print(f"   Priority: {task['priority']} | {status} | Deadline: {deadline}")


def complete(tasklist,choice1):
    if tasklist[choice1 - 1]["status"]:
        print("The task already marked as Complete")

    else:
        tasklist[choice1 - 1]["status"] = True
        print("The task is marked as Complete")


def incomplete(tasklist,choice2):
    if not tasklist[choice2 - 1]["status"]:
        print("The task already marked as Incomplete")

    else:
        tasklist[choice2 - 1]["status"] = False
        print("The task is marked as Incomplete")


def load_tasks():
    try:
        with open("task-manager.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasklist):
    with open("task-manager.json", "w") as f:
        json.dump(tasklist, f, indent=2)




main()






