import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors"))
print(game[user_choice])

computer_choice = random.randint(0, (len(game)-1))
print(f"Computer chose\n: {game[computer_choice]}")

if (user_choice == 0 and computer_choice == 1):
  print("Computer wins")
elif (user_choice == 0 and computer_choice == 2):
  print("You win")
elif (user_choice == 1 and computer_choice == 0):
  print("You win")
elif (user_choice == 1 and computer_choice == 2):
  print("Computer wins")
elif (user_choice == 2 and computer_choice == 0):
  print("Computer wins")
elif (user_choice == 2 and computer_choice == 1):
  print("You wins")
else:
  print("It's a tie!")