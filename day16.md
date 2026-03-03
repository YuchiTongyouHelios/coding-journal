# Day 16: Return vs Print – The Moment It Clicked

## What I Built Today
- A calculator function that RETURNS results instead of printing them
- Tested the difference between print() and return with multiple examples

## What I Learned
- `print()` sends output to the screen but returns `None`
- `return` sends data back to where the function was called
- Functions that return data can be used in expressions (like `calculator(10,5,'+') + 10`)
- `input()` and `len()` are functions that return values – I've been using return all along
- Python evaluates expressions first, THEN returns the result

## One Thing I Struggled With
- Kept trying to `return +` instead of `return a + b`
- Didn't understand why `print()` functions gave me `None`
- The bakery analogy finally made it click: print = shouting, return = handing over

## My Code (End of Day 16)
```python
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
print(calculator(10, 5, '+'))
print(calculator(10, 5, '-')) 
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))
print(f"10 + 5 = {result}")
