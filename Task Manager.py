import heapq

# Task class to hold task details and priority
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    # Define comparison methods for priority queue (heap)
    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"Task: {self.name}, Priority: {self.priority}"

# Task Management System Class
class TaskManagementSystem:
    def __init__(self):
        self.active_tasks = []  # Min-Heap to store tasks by priority
        self.completed_tasks = []  # Dynamic array (list in Python) for completed tasks

    # Add a new task with a priority
    def add_task(self, name, priority):
        task = Task(name, priority)
        heapq.heappush(self.active_tasks, task)
        print(f"Added: {task}")

    # Complete the highest priority task
    def complete_task(self):
        if self.active_tasks:
            completed_task = heapq.heappop(self.active_tasks)
            self.completed_tasks.append(completed_task)
            print(f"Completed: {completed_task}")
        else:
            print("No tasks to complete.")

    # View tasks by priority
    def view_active_tasks(self):
        if not self.active_tasks:
            print("No active tasks.")
        else:
            print("Active Tasks (by priority):")
            for task in sorted(self.active_tasks):
                print(task)

    # View completed tasks
    def view_completed_tasks(self):
        if not self.completed_tasks:
            print("No completed tasks.")
        else:
            print("Completed Tasks:")
            for task in self.completed_tasks:
                print(task)

    # Search for a task in active tasks
    def search_task(self, task_name):
        for task in self.active_tasks:
            if task.name == task_name:
                print(f"Found Task: {task}")
                return
        print("Task not found.")

# Main program to interact with the Task Management System
if __name__ == "__main__":
    system = TaskManagementSystem()
    
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Active Tasks")
        print("4. View Completed Tasks")
        print("5. Search for a Task")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task_name = input("Enter task name: ")
            task_priority = int(input("Enter task priority (lower value = higher priority): "))
            system.add_task(task_name, task_priority)
        elif choice == 2:
            system.complete_task()
        elif choice == 3:
            system.view_active_tasks()
        elif choice == 4:
            system.view_completed_tasks()
        elif choice == 5:
            search_name = input("Enter the task name to search: ")
            system.search_task(search_name)
        elif choice == 6:
            print("Exiting Task Management System.")
            break
        else:
            print("Invalid choice! Please select a valid option.")
