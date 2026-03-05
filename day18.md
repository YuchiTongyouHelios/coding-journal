# Day 18: Drilling Loops, Lists, and File I/O

## What I Built Today
Fixed the gaps in my understanding by drilling three core concepts using my To-Do app as the example.

## What I Drilled

### 1. Loops – Three Ways to Loop Through a List
```python
tasks = ["buy milk", "walk dog", "pay bills"]

# Way 1: for loop with range (best for numbered lists)
print("Your tasks:")
for i in range(len(tasks)):
    print(f"{i+1}. {tasks[i]}")
```
# Way 2: for loop directly (when you don't need numbers)
```python
print("\nYour tasks:")
for task in tasks:
    print(f"- {task}")
```
# Way 3: while loop (more control)
```python
print("\nYour tasks:")
index = 0
while index < len(tasks):
    print(f"{index+1}. {tasks[index]}")
    index += 1
```
2. List Operations
```python
print(f"Number of tasks: {len(tasks)}")
print(f"First task: {tasks[0]}")
print(f"Last task: {tasks[-1]}")
print(f"First 2 tasks: {tasks[:2]}")

if "walk dog" in tasks:
    print("Walk dog is on the list")

if "pay bills" in tasks:
    position = tasks.index("pay bills")
    print(f"Pay bills is at position {position}")  # Computer index (0,1,2)
    print(f"User would see it as number {position + 1}")  # Human number (1,2,3)
```
3. File I/O with Error Handling
```python
def save_tasks():
    try:
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
            print("Tasks saved!")
    except:
        print("Error saving tasks")

def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r") as f:
            tasks = []
            for line in f:
                tasks.append(line.strip())
        print(f"Loaded {len(tasks)} tasks.")
    except FileNotFoundError:
        print("No save file found. Starting fresh.")
        tasks = []
    except:
        print("Error loading file. Starting fresh.")
        tasks = []
```
## What I Learned
File modes: "w" = write (overwrites), "r" = read, "a" = append

f is just a variable – could be named anything (file, handle, etc.)

List comprehension [line.strip() for line in f] is shorthand for a loop

index() method finds the position of an item in a list (returns computer index)

Computer vs Human: Always translate between 0-based indexes and 1-based user numbers

## One Thing I Struggled With
Kept writing task[0] instead of tasks[0] – variable names matter!

Forgot that global tasks is needed when modifying a global list inside a function

Had to think through why position + 1 is needed for user display

## What Clicked Today
index() is like asking Python "where is this in the list?"

The three loop styles each have different use cases

Error handling makes programs robust instead of crashy

Drilling old concepts makes new ones easier to understand
