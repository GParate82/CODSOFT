import json
import os

class ToDoList:
    def __init__ (self, filename = 'todo.json'):
        self.filename = filename
        self.load_task()

    def load_task(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.task = json.load(file)

        else:
            self.task = []

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.task, file, indent = 4)

    def add(self, task):
        self.task.append({'task' : task, 'done' : False})
        self.save()
        print(f' Added task: "{task}"')

    def update(self, index, new_task):
        if 0 <= index < len(self.task):
            old_task = self.task[index]['task']
            self.task[index]['task'] = new_task
            self.save()
            print(f' Updated task {index} from "{old_task}" to "{new_task}"')
        else:
            print(f' No task found at index {index}....!!!!!')

    def delete(self, index):
        if 0 <= index < len(self.task):
            removed_task = self.task.pop(index)
            self.save()
            print(f' Removed task: "{removed_task["task"]}"')
        else:
            print(f' No task found at index {index}....!!!!!')

    def completed(self, index):
        if 0 <= index < len(self.task):
            self.task[index]['done'] = True
            self.save()
            print(f' Completed task {index}')
        else:
            print(f' No task found at index {index}....!!!!!')

    def view(self):
        if not self.task:
            print('No task found...!!!')
        else:
            for index, task in enumerate(self.task):
                status = 'Done' if task['done'] else 'Not Done'
                print(f' {index}. {task["task"]} - {status}')

def main():
    todoList = ToDoList()

    while True:
        print("\n.......... Options for To-Do List............\n")
        print("1. Add task\n")
        print("2. Update task\n")
        print("3. Delete task\n")
        print("4. Mark task as complete\n")
        print("5. View task\n")
        print("6. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todoList.add(task)

        elif choice == '2':
            index = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")
            todoList.update(index, new_task)

        elif choice == '3':
            index = int(input("Enter task number to delete: "))
            todoList.delete(index)

        elif choice == '4':
            index = int(input("Enter task number to mark as complete: "))
            todoList.completed(index)

        elif choice == '5':
            todoList.view()

        elif choice == '6':
            print("Exited.....")
            break

        else:
            print("Invalid choice. Please choose between 1-5.")

if __name__ == "__main__":
    main()