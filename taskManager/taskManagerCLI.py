import json
import datetime

print("Welcome to your Task Manager. Please enter your option")
print("1. List all tasks")
print("2. Add a task")
print("3. Update a task")
print("4. Delete a task")
print("5. Exit")

#Get user input
while True:
    option = int(input("Enter your option:"))

    if option < 1 or option > 5:
        raise Exception("Invalid option selected. Please select a valid option")

    #Review the tasks
    if option == 1:
        with open("tasks.json","r") as file:
            tasks = json.load(file)
        print("Select your option to display your tasks:")
        print("a. All tasks")
        print("b. Only pending tasks")
        print("c. Only completed tasks")
        opt = input("Enter your option:")
        if opt == "a":
            for task in tasks['task_details']:
                print(task["id"],  task["title"], task["status"])
        elif opt == "b":
            for task in tasks['task_details']:
                if task["status"] == "In Progress" or task["status"] == "Not Started":
                    print(task["id"],  task["title"])
        elif opt == "c":
            for task in tasks['task_details']:
                if task["status"] == "Done":
                    print(task["id"],  task["title"])
        else:
                print("No tasks found for the selected option")
                break
        file.close()
    

    #Add a task
    elif option == 2:
        with open("tasks.json","r") as file:
            tasks = json.load(file)
            task = {}
            task["id"] = int(input("Enter the task id:"))
            task["title"] = input("Enter the task title:")
            task["status"] = input("Enter the task status:")
            task["createdAt"] = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            task["updatedAt"] = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            tasks['task_details'].append(task)
            with open("tasks.json","w") as file:
                json.dump(tasks,file)
        file.close()
        print(f"Task created successfully with ID {task['id']} at {datetime.datetime.now()}")

    #Update the status of a task
    elif option == 3:
        with open("tasks.json","r") as file:
            tasks = json.load(file)
        task_id = int(input("Enter the task id to update:"))
        for task in tasks['task_details']:
            if task["id"] == task_id:            
                task["status"] = input("Enter the task status:")
                task["updatedAt"] = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                break
        with open("tasks.json","w") as file:
            json.dump(tasks,file)
        file.close()
        print(f"Task with ID {task['id']} updated successfully at {datetime.datetime.now()}")

    #Delete a task
    elif option == 4:
        with open("tasks.json","r") as file:
            tasks = json.load(file)
        task_id = int(input("Enter the task id to delete:"))
        for task in tasks['task_details']:
            if task["id"] == task_id:            
                tasks['task_details'].remove(task)
                break
        with open("tasks.json","w") as file:
            json.dump(tasks,file)
        file.close()
        print("Task deleted successfully")

    #Exit the program
    else:
        print("Thank you for updating the tasks. Have a great day!")
        exit()
