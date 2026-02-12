
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
