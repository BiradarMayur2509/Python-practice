import json

# show menu
def show_menu():
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("$. Exit")
    
# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("taask added")
    
# View tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No task Found")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            
# delete task

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete:")) - 1
        revomed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {revomed}")
    except:
        print("Invalid input!")
    
# Load task from file 
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return[]
    
# save tasks to file 

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        
        
# Main function

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Choose Option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!") 
            
# Run app
if __name__ == "__main__":
    main()
