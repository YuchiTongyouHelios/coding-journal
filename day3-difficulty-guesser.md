# Day 3: Added Difficulty Levels

## What I Built
I took my number guessing game from Day 2 and added difficulty levels. Now the user can choose Easy (1-10), Medium (1-50), or Hard (1-100).

## The Code
```python
import random

print("Choose difficulty:")
print("1 - Easy (1-10)")
print("2 - Medium (1-50)")
print("3 - Hard (1-100)")

difficulty = input("Enter 1, 2, or 3: ")

if difficulty == "1":
    max_number = 10
elif difficulty == "2":
    max_number = 50
elif difficulty == "3":
    max_number = 100
else:
    print("Invalid choice. Defaulting to Easy.")
    max_number = 10

secret = random.randint(1, max_number)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input(f"Guess a number 1-{max_number}: "))
    attempts = attempts + 1
    
    if guess == secret:
        print("You got it!")
        print(f"You took {attempts} tries.")
    elif guess < secret:
        print(f"Too low. Guess between 1-{max_number}.")
    else:
        print(f"Too high. Guess between 1-{max_number}.")
```
## What I Learned
if/elif/else chains let you handle multiple choices

f-strings (f"text {variable}") insert variables directly into text

User choice can control game behavior

Default cases (like else) handle invalid input

## Problems I Fixed
Wrong range in prompt – I forgot to update the input message. Fixed with f-string.

Invalid choice crash – Added else to default to Easy.

Hints still showed 1-10 – Updated both "too low" and "too high" messages.
