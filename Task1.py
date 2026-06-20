tasks=[]

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View tasks \n2. Add a task \n3. Mark a task as done \n4. Delete a task \n5. Exit")
    print("======================")

def view_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty!")
        return
    
    print("\nYour Tasks:")
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['text']} [{status}]")

def add_task():
    task_text = input("\nEnter the new task: ")
    new_task = {"text": task_text, "done": False}
    tasks.append(new_task)
    print(f"Task '{task_text}' added!")

def mark_done():
    view_tasks()
    if len(tasks) == 0:
        return
    
    choice = input("\nEnter the task number to mark as done: ")

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True 
            print(f"Task '{tasks[index]['text']}' marked as done!")
        else:
            print("Invalid task number. ")
    else:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    
    choice = input("\nEnter the task number to delete: ")

    if choice.isdigit():
        index = int(choice) - 1 
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task['text']}' deleted!")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

def main():
    print("Welcome to your To-Do List App!")
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! Have a productive day!")
            break
        else:
            print("Invalid optiobn. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()
    