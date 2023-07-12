
from art import logo
from art import vs
from replit import clear
from game_data import data
import random


def compare(A, B):
  if A>B:
    return "A"
  else:
    return "B"


def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def game():
  game_is_on = True
  score = 0

  PlayerA = random.choice(data)
  PlayerB = random.choice(data)
  
  
  while game_is_on:

    PlayerA = PlayerB
    PlayerB = random.choice(data)

    while PlayerA == PlayerB:
      PlayerB = random.choice(data)

    A = PlayerA["follower_count"]
    B = PlayerB["follower_count"]
    
    print(logo)
    print(f"Compare A: {format_data(PlayerA)}.")
    print(vs)
    print(f"Against B: {format_data(PlayerB)}.")
    guess = input("Who has more followers? Type 'A' or 'B'")

    ans = compare(A, B)

    clear()
    if guess == ans:
      score += 1
      print(f"You're right! Current score: {score}")
      
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game_is_on = False


game()
