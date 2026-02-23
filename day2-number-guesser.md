# Day 2: Number Guessing Game

## What I Built
A game where the computer picks a random number and you guess it.


## What I Learned
While loops repeat until a condition is met

Indentation tells Python what belongs together

Where you put your code changes when it runs

Random numbers need import random

## Problems I Fixed
Forgot import random → code crashed

Elif was indented wrong → hints didn't show

Attempt counter only showed 1 → moved it inside while loop

## Code
import random

secret = random.randint(1, 10)

guess = 0

attempts = 0

while guess != secret:
  
    guess = int(input("Guess a number 1-10: "))
  
    attempts = attempts + 1
    
    if guess == secret:

    
        print("You got it!")
      
        print("You took", attempts, "tries.")
      
    elif guess < secret:
      
        print("Too low, try again.")
      
    else:
      
        print("Too high, try again.")
