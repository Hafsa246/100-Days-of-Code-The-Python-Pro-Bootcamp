age = 90
user_age = int(input("What is your current age? "))

age_left = age - user_age

days = age_left*365
months = age_left*12
weeks = age_left*52

print(f"You have {days} days, {weeks} weeks, and {months} months left.")