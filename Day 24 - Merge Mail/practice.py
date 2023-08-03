# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

## By default, the mode is read-only. Deletes all text and re-write new
# If you write in a file that doesn't exist, then the computer will create a new file with that name
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

## If you want to add text use append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")


with open("C:/Users/hafsa/Dropbox/My PC (DESKTOP-9HJDI1B)/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
