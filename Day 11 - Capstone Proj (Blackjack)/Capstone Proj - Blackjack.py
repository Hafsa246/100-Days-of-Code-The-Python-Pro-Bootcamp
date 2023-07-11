from art import logo
from replit import clear
import random

def pick_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def score(card):
  if sum(card) == 21 and len(card) == 2:
    return 0
  
  if 11 in card and sum(card)>21:
    cards.remove(11)
    cards.append(1)

  return sum(card)


def compare(your_score, comp_score):
  if your_score > 21 and comp_score > 21:
    return "You went over. You lose 😤"

  if your_score == comp_score:
    return "Draw 🙃"
  elif comp_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif your_score == 0:
    return "Win with a Blackjack 😎"
  elif your_score > 21:
    return "You went over. You lose 😭"
  elif comp_score > 21:
    return "Opponent went over. You win 😁"
  elif your_score > comp_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_game():
  print(logo)

  your_cards = []
  comp_cards = []
  is_game_over = False

  while not is_game_over:

    for _ in range(2):
      your_cards.append(pick_card())
      comp_cards.append(pick_card())

    your_score = score(your_cards)
    comp_score = score(comp_cards)

    print(f"   Your cards: {your_cards}, current score: {your_score}")
    print(f"   Computer's first card: {comp_cards[0]}")

    if your_score == 0 or comp_score == 0 or your_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        your_cards.append(deal_card())
      else:
        is_game_over = True

  while comp_score != 0 and compr_score < 17:
    comp_cards.append(deal_card())
    comp_score = score(comp_cards)

  print(f"   Your final hand: {your_cards}, final score: {your_score}")
  print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()