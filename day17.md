# Day 17: Foundation Review – Variables, Types, I/O

## What I Built Today
Three tiny programs to drill Week 1-2 basics:

1. **Type Checker** – Shows what type Python sees
2. **Simple Calculator** – Does math with operator choice
3. **Personal Info Form** – Collects and displays user data

## What I Reviewed
- `input()` always gives strings
- `type()` tells you what kind of data something is
- `int()` converts strings to numbers (but can crash)
- `try/except` catches conversion errors
- `if/elif/else` vs multiple `if` statements (learned this the hard way)
- Division by zero needs explicit checking

## One Thing I Struggled With
Used multiple `if` statements instead of `elif`, so my `else` kept triggering. Had to trace through line by line to see why "Invalid operation" showed up even when operation was valid.

Also forgot that `return` is only for functions – tried using it in script and got errors.

## My Code (End of Day 17)

### Program 1: Type Checker
```python
user_input = input("Please enter something: ")
print(f"You wrote: {user_input}")
print(f"Python sees it as: {type(user_input)}")

try:
    as_int = int(user_input)
    print(f"As integer: {as_int}, type: {type(as_int)}")
except ValueError:
    print("Couldn't convert to int – it's not a number")
```
## Program 2: Simple Calculator
```python
first_number = int(input("Please enter first number: "))
second_number = int(input("Please enter second number: "))
operation = input("Please enter operation (+, -, *, /): ")

if operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    if second_number == 0:
        result = "Can't divide by zero"
    else:
        result = first_number / second_number
else:
    result = "Invalid operation"

print(f"Result: {result}")
```
## Program 3: Personal Info Form
```python
name = input("What is your name? ")
city = input("Which city do you live in? ")

try:
    age = int(input("How old are you? "))
    print(f"{name} is {age} years old and lives in {city}.")
except ValueError:
    print("That's not a valid age. Please enter a number.")
```
## What Clicked Today
try/except goes around the line that might fail, not after it

elif chains are one decision, multiple ifs are separate decisions

return has no place outside functions

Drilling old concepts made new concepts (like return) make more sense

Still Fuzzy?
Nothing major – today was about solidifying
