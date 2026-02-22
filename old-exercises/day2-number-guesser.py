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
