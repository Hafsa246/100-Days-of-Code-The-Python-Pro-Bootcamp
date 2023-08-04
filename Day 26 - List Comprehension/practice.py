# List Comprehension 
# new_list = [new_item for item in old_list if test]

numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]

name = "Angela"
new_name = [n for n in name]

new_list = [n*2 for n in range(1,5)]

names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 4]
