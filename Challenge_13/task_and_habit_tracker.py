def main():
    tasks = []
    try:
        with open ('tasks.txt', 'r') as f:
            for line in f:
                task_title, task_type, task_condition, task_streak = line.removesuffix("\n").strip().split(",")
                if task_type in ("daily", "one-time") and task_condition in ("True", "False") and task_streak.isnumeric():
                    if task_condition == "True":
                        task_condition = True
                    elif task_condition == "False":
                        task_condition = False
                    tasks.append({
                        "title": task_title,
                        "type": task_type,
                        "completed": task_condition,
                        "streak": int(task_streak)
                    })
                else:
                    print(f"{task_title} contains inavlid data. It won't be added")
                    continue
    except FileNotFoundError:
        print("File not found")
        
    while True:
        
        print("")
        
        user_choice = get_option()
        
        if user_choice == 1:
            output = add_new_task(tasks)
            if output is not None:
                tasks.append(output)
            
        elif user_choice == 2:
            mark_task_as_completed(tasks)
            
        elif user_choice == 3:
            view_all_tasks(tasks)
            
        elif user_choice == 4:
            view_pending_tasks(tasks)
            
        elif user_choice == 5:
            view_completed_tasks(tasks)
            
        elif user_choice == 6:
            view_daily_streaks(tasks)
            
        elif user_choice == 7:
            save(tasks)
            break
            
def get_option():
    while True:
        print("")
        print("1. Add new task")       
        print("2. Mark task as completed")       
        print("3. View all tasks")       
        print("4. View pending tasks")       
        print("5. View completed tasks")       
        print("6. View daily streaks")             
        print("7. Save & exit")       
            
        user_input = (input("Choose an option: "))
        
        if not user_input.isnumeric() or not int(user_input) in range(1, 8):
            print("Not a valid option.")
            continue
        else:
            return int(user_input)
        
# prompt the user for a title and a type to then return the dictionary of a new task
def add_new_task(tasks):
    task_title = input("Task title (or 'cancel' to terminate operation): ").lower().lstrip().rstrip()
    
    if task_title == "cancel":
        print("No update was made.")
        return
    else:
        for task in tasks:
            if task_title == task["title"]:
                print(f"{task_title} already exists. It won't be added.")
                return
    
    while True:
        task_type = input("Task type ('daily' or 'one-time'. Type 'cancel' if you want to terminate operation): ").lower().strip()
        
        if task_type == "cancel":
            print("No update was made.")
            return
        elif task_type not in ("daily", "one-time"):
            print("Invalid task type. Please try again.")
            print("")
        else:
            new_task = {
                "title": task_title,
                "type": task_type,
                "completed": False,
                "streak": 0
            }
            print(f"{task_title} added successfully.")
            return new_task
        
# mark existsing task as complete if its a one_time type and increase its streak if its a daily type
def mark_task_as_completed(tasks):
    task_title = input("Task title (or 'cancel' to terminate operation): ").lower().lstrip().rstrip()

    if task_title == "cancel":
        print("No update was made.")
        return
    else:
        titles = []
        for task in tasks:
            titles.append(task["title"])
        if not task_title in titles:
            print(f"{task_title} doesn't exist.")
            return
        else:
            for task in tasks:
                if task["title"] == task_title:
                    if task["type"] == "daily":
                        task["streak"] += 1
                        print(f"{task_title} updated. Current streak: {task['streak']}")
                        return
                    else:
                        if task["completed"] == True:
                            print(f"{task_title} already marked as completed.")
                        else:
                            task['completed'] = True
                            print(f"{task_title} now marked as completed.")
                            return
                
# prints all tasks and their info
def view_all_tasks(tasks):
    for task in tasks:
        print(f"{task['title']} - type: {task['type']}, completed: {task['completed']}, streak: {task['streak']}")
    return

# prints non completed tasks and their info
def view_pending_tasks(tasks):
    count = 0
    for task in tasks:
        if task["completed"] == False:
            count += 1
            print(f"{task['title']} - type: {task['type']}, completed: {task['completed']}, streak: {task['streak']}")
        else:
            continue
    if count == 0:
        print("No incompleted tasks found.")
        
    return

# prints completed tasks and their info
def view_completed_tasks(tasks):
    count = 0
    for task in tasks:
        if task["completed"] == True:
            count += 1
            print(f"{task['title']} - type: {task['type']}, completed: {task['completed']}, streak: {task['streak']}")
        else:
            continue
    if count == 0:
        print("No completed tasks found.")
        
# prints daily the tasks and their streaks
def view_daily_streaks(tasks):
    count = 0
    for task in tasks:
        if task["type"] == "daily":
            count += 1
            print(f"{task['title']} - streak: {task['streak']}")
        else:
            continue
    if count == 0:
        print("No daily tasks found.")
        
# saves data to an external file
def save(tasks):
    with open ("tasks.txt", 'w') as f:
        for task in tasks:
            f.write(f"{task['title']},{task['type']},{task['completed']},{task['streak']}\n")
            
    print("File updated.")
    return

    

if __name__ == "__main__":
    main()