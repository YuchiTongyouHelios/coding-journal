# Day 23: Building My First Functions

## What I Built Today
A Mad Libs game that asks for words and builds a story.

## What I Learned
- **Functions = my own custom words** in Python
- **return** sends data back (like a vending machine giving your snack)
- **Parameters** are the inputs a function needs
- My code worked first try! 💪

## My Code
```python
adjective = input("Enter an adjective.")
noun = input("Enter a noun.")
verb = input("Enter a verb.")
adverb = input("Enter an adverb.")
story = f"The {adjective} {noun} {verb} {adverb} through the forest."
print("\n" + "="*40)
print("YOUR STORY")
print(story)
print("="*40)
```

## Key Takeaway
I can start with simple code that works, THEN wrap it in functions to organize it better.

## What's Next
Add a "play again" feature so the game doesn't just end.
