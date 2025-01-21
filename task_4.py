from collections import Counter

text = """

python is an amazing programming language, python is fun to learn and powerful to use 

        """ 
words = text.lower(). split()
word_count = Counter(words)

print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
print (len (text))

from queue import Queue

# create a task queue
task_queue = Queue()

# add tasks to the queue 
tasks = ["Task 1: Clean the room", "Task2: Write Python code", "Task 3: Read a book"]
for task in tasks:
    task_queue.put(task)

# process tasks 
print("Processing tasks:")
while not task_queue.empty():
    print(task_queue.get())

    

