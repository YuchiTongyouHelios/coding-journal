# Day 1: Personal Info Bot

## What I Built
A program that asks for your name, last name, and birth year, then tells you your age and initials.

## The Code
```python
print("=" * 30)
print("Personal Info Bot")
print("=" * 30)

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
birth_year = int(input("What year were you born? "))

print("Hello,", first_name, last_name)
print("You are about", 2025 - birth_year, "years old")
print("Your initials are", first_name[0] + "." + last_name[0] + ".")
```

## What I Learned
print() shows things on screen

input() asks the user for text

int() converts text to numbers

Variables store information like first_name

[0] gets the first letter of a string

+ joins text together

## Problems I Fixed
Variable names – I first wrote first[0]name which is invalid. Fixed to first_name.

Commas in print – I forgot commas between items. Fixed.

Initials didn't show – I typed my name with spaces like "j o h n". Python counted the spaces. Fixed by typing normally.

Spacing before elif – Wrong indentation made hints not show. Fixed by lining up if, elif, else
