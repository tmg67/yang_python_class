from collections import deque

task_manager = deque ([f"{todo}" for todo in
               ["1. to do home work","2. to do cleaning"]])
task_manager.append("3. to do laundry")
print(task_manager)
print("task is added")
task_manager.popleft()
print("task is removed")
task_manager.rotate(3)
print(task_manager)
print("task is rotated")

