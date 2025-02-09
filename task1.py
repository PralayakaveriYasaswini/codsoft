class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\nTo-Do List")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                task = input("Enter task: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_number = int(input("Enter task number to mark as completed: "))
                self.mark_task_completed(task_number)
            elif choice == "4":
                task_number = int(input("Enter task number to delete: "))
                self.delete_task(task_number)
            elif choice == "5":
                print("Exiting To-Do List.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ToDoList().run()
