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
