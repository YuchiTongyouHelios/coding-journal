# Day 4: Added "Play Again?"

## What I Built
I took my number guesser from Day 3 and added a loop that lets the player keep playing until they say "no".

## The Code
```python
# Day 4: Added "Play Again?"

## What I Built
I took my number guesser from Day 3 and added a loop that lets the player keep playing until they say "no".

## The Code
```python
import  random
playing = True
while playing: 
    attempts = 0
    print ("Choose difficulty:")
    print ("1 - Easy (1-10)")
    print ("2 - Medium (1-50)")
    print ("3 - Hard (1-100)")
    difficulty = input("Enter 1,2 or 3: ")
    if difficulty == "1":
        max_number = 10
    elif difficulty == "2":
        max_number = 50
    elif difficulty == "3":
        max_number = 100
    else:
        print("Invalid choice, Defaulting to Easy.")
        max_number = 10
    secret = random.randint(1, max_number)
    attempts = 0
    guess = 0
    while guess != secret:
        guess = int(input(f"Guess the number 1-{max_number}: "))
        attempts = attempts + 1
        if guess == secret:
            print ("You got it!")
            print (" You took" , attempts , "attempts")
        elif guess < secret:
            print (f"Too low, Guess between 1-{max_number}.")
        else:
            print (f"Too high, Guess between 1-{max_number}")
    play_again = input ("Play again? (yes/no): ")
    if play_again != "yes":
        playing = False
print ("Thanks for playing!")
```
## What I Learned
Outer loops can wrap an entire game

Indentation determines what runs inside the loop

playing = True/False controls whether the loop continues

Reset variables like attempts inside the loop for each new round

## Problems I Fixed
Play again question never showed – I had put it outside the loop. Fixed by moving it inside.

Import random inside loop – Caused an error. Moved it to the top.

Indentation errors – Fixed by making sure everything under while playing: was indented.

## Proof
Choose difficulty:
1 - Easy (1-10)
2 - Medium (1-50)
3 - Hard (1-100)
Enter 1,2 or 3: 1
Guess the number 1-10: 5
Too high, Guess between 1-10.
Guess the number 1-10: 2
You got it!
You took 2 attempts
Play again? (yes/no): yes

Choose difficulty:
1 - Easy (1-10)
2 - Medium (1-50)
3 - Hard (1-100)
Enter 1,2 or 3: no
Thanks for playing!
