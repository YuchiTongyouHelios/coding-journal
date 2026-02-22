import random
from datetime import date
try:
    with open("high_score.txt", "r") as f:
        high_score = int(f.read())
except FileNotFoundError:
    high_score = None
    high_score_date = ""
playing = True
total_wins = 0
total_attempts = 0
while playing:
    guess = 0
    attempts = 0
    print ("Choose a difficulty")
    print ("1 = Easy (1-10)")
    print ("2 = Medium (1-50)")
    print ("3 = Hard (1-100)")
    choice = input("Choose a difficulty (1,2 or 3)")
    if choice == "1":
        max_num = 10
    elif choice == "2":
        max_num = 50
    elif choice == "3":
        max_num = 100
    else:
        print ("Invalit choice, defaulting to Easy")
        max_num = 10

    secret = random.randint (1, max_num)
    while guess != secret:
        guess = int(input(f"Choose a number between 1-{max_num}."))
        attempts += 1
        if guess > secret:
            print ("Too high, try again!")
        elif guess < secret:
            print ("Too low, try again!")
    else:
        print (f"You got it in {attempts} attempts!")
        total_wins = total_wins + 1
        total_attempts = total_attempts + attempts
        print (f"Total wins: {total_wins}")
        print (f"Total attempts: {total_attempts}")
        if high_score is None or attempts < high_score:
            high_score = attempts
            print (f"New high score! {attempts} attempts")
            high_score_date = str(date.today())
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
            with open("high_score_date.txt", "w") as f:
                f.write(high_score_date)
        else:
            print (f"High score: {high_score} attempts {high_score_date}")
        play_again = (input("Do you want to play again? (yes/no)")).lower()
    if play_again != "yes":
        with open("high_score.txt", "w") as f:
            f.write(str(high_score))
        with open("high_score_date.txt", "w") as f:
            f.write(high_score_date)
        print ("Thanks for playing!")
        break
