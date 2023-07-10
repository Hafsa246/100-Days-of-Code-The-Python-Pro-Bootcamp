from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

bidders = {}
game = True

print(logo)
print("Welcome to the secret auction program.")

while game:
  
  person = input("What is your name? ")
  bid = int(input("What is your bid? "))

  bidders[person] = bid

  ans = input("Are there any other bidders? Type 'yes' or 'no'")

  highest_bidder = 0
  name = ""
  
  for i in bidders:
    if bidders[i] > highest_bidder:
      highest_bidder = bidders[i]
      name = i
  
  
  if ans == "no":
    print(f"The winner is {name} with a bid of ${highest_bidder}")
    game = False
  else:
    clear()
