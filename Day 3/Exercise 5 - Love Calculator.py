# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine = name1+name2
name = combine.lower()
True1 = 0
Love = 0

for i in name:
    if(i == "t" or i == "r" or i == "u" or i == "e"):
        True1 += 1


for i in name:
    if(i == "l" or i == "o" or i == "v" or i == "e"):
        Love += 1

    
num = True1*10 + Love

if(num<=10 or num>=90):
    print(f"Your score is {num}, you go together like coke and mentos.")
elif(num >= 40 and num <= 50):
    print(f"Your score is {num}, you are alright together.")
else:
    print(f"Your score is {num}.")
