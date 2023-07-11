from art import logo
from random import randint
print(logo)

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 to 100")
num = randint(1, 101)
print(f"Psst! The correct answer is {num}")

easy = 10
hard = 5

difficulty = input("Choose a difficulty level, 'Easy' or 'Hard': ")


def compare(guess):
  if guess == num:
    return "Correct"
  elif guess < num:
    return "Too Low"
  elif guess > num:
    return "Too high"



if difficulty == "easy":
  if easy == 0:
    print("You've run out of guesses, you lose.")
  
  while easy != 0:
    print(f"You have {easy} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    guessing = compare(guess)

    if guessing == "Correct":
      print(f"You got it. The answer is {num}")
      easy = 0
    else:
      print(guessing)
      print("Guess again")
      easy -= 1

else:
  if hard == 0:
    print("You've run out of guesses, you lose.")
  while hard != 0:
    print(f"You have {hard} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    guessing = compare(guess)

    if guessing == "Correct":
      print(f"You got it. The answer is {num}")
      hard = 0
    else:
      print(guessing)
      print("Guess again")
      hard -= 1