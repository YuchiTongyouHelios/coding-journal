# Day 5: Added Score Tracking

## What I Built
I added stats to my number guesser. Now it tracks total wins and total attempts across all rounds.

## The Code
```python
import  random
total_wins = 0
total_attempts = 0
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
            total_wins = total_wins + 1
            total_attempts = total_attempts + attempts
            print (f"Total wins: {total_wins}")
            print (f"Total_attempts: {total_attempts}")
        elif guess < secret:
            print (f"Too low, Guess between 1-{max_number}.")
        else:
            print (f"Too high, Guess between 1-{max_number}")
    play_again = input ("Play again? (yes/no): ")
    if play_again != "yes":
        playing = False
print ("Thanks for playing!")
print ("\n FINAL STATS:")
print (f"Wins: {total_wins}")
print (f" Total attempts: {total_attempts}")
```

## What I Learned
Global variables (total_wins, total_attempts) remember values across loops

Where you put variables matters – outside the main loop = permanent, inside = resets each round

f-strings make displaying stats clean

Final stats can show after the game ends

## Problems I Fixed
Stats resetting each round – Fixed by moving counters outside the main loop

Wrong attempt count – Made sure to add attempts to total_attempts after each win

Stats didn't show – Added print statements inside the win condition

## Proof
Choose difficulty:
1 - Easy (1-10)
2 - Medium (1-50)
3 - Hard (1-100)
Enter 1, 2, or 3: 1
Guess a number 1-10: 5
Too high...
Guess a number 1-10: 2
You got it in 2 tries!
Total wins: 1
Total attempts: 2

Play again? (yes/no): yes
... (next round)
