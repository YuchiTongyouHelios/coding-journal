# Day 19: Return Values Everywhere – No Prints Inside Functions

## What I Built Today
Rewrote my To-Do app functions to RETURN strings instead of PRINTING them. Main loop now handles all printing.

## What I Learned
- Functions should RETURN data, not print it
- Parameters let you pass VALUES into functions
- The variable name inside a function doesn't matter – only the value
- Building strings with `+=` lets you collect multiple lines
- Main code calls functions and prints what they return

## One Thing I Struggled With
- Kept putting `print()` inside functions out of habit
- Forgot that parameters need to be passed in from the caller
- Mixed up parameter names and used undefined variables

## My Code (End of Day 19)

### show_tasks() – Returns a string
```python
def show_tasks():
    if not tasks:
        return "No tasks yet."
    else:
        result = ""
        for i in range(len(tasks)):
            result += f"{i+1}. {tasks[i]}\n"
        return result
```
search_tasks() – Takes a term, returns results
```python
def search_tasks(search_term):
    result = ""
    for i in range(len(tasks)):
        if search_term.lower() in tasks[i].lower():
            result += f"{i+1}. {tasks[i]}\n"
    if result == "":
        return "No tasks match your search."
    else:
        return result
```
add_task() – Takes new task, returns message
```python
def add_task(new_task):
    if new_task == "":
        return "Cannot add empty task."
    tasks.append(new_task)
    save_tasks()
    return f"Task '{new_task}' added!"
```
Main loop (now just prints what functions return)
```python
while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Mark a task complete")
    print("5. Search tasks")
    print("6. Quit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        new = input("Enter task: ")
        print(add_task(new))  # Print what function returns
    
    elif choice == "2":
        print(show_tasks())  # Print what function returns
    
    elif choice == "5":
        term = input("Enter search term: ")
        print(search_tasks(term))  # Print what function returns
```
## What Clicked Today
Functions are like machines: give them input (parameters), they give back output (return)

The main code is the manager – it asks for input, passes it to functions, and displays results

return is the only way to get data OUT of a function

Once I stopped printing inside, the code became more flexible

## Still Fuzzy?
Need more practice with parameters – remembering to pass things in

But the pattern is starting to make sense
