from queue import Queue

#create a task queue
task_queue = Queue()

#add tasks to the queue
tasks = ["task 1: clean the room", "Task 2: Write python code", "task 3: read a book"]
for task in tasks:
    task_queue.put(task)

#process tasks
print("processing tasks:")
while not task_queue.empty():
    print(task_queue.get())