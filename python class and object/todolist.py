class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)
        print(f"task'{task}'added to the list")

    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("ftask'{task}'removed from the list")
        else:
            print(f"task'{task}' not found in the list")
    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"task updated to '{new_task}'.")
        else:
            print(f"task'{old_task}' not found in list")
    def show_tasks(self):
        if self.tasks:
            print("your todo list")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1 }. {task}")
        else:
            print("your todo list is empty.")

todo_list = TodoList()

todo_list.add_task("buy groceries")
todo_list.add_task("finish  the report")
todo_list.add_task("call mom")

todo_list.show_tasks()
todo_list.remove_task("finish the report")
todo_list.update_task("buy groceries", "go for a walk")
todo_list.show_tasks()