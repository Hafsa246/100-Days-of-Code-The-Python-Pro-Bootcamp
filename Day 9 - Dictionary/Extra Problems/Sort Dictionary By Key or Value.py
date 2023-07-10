# Example 1: Sort Dictionary By Key in Python

myDict = {
    'ravi': 10, 
    'rajnish': 9,
    'sanjeev': 15,
    'yash': 2, 
    'suraj': 32
}

new_dict = dict(sorted(myDict.items()))

print(new_dict)


# Example 2

key_value = {}

key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

new_dict1 = dict(sorted(key_value.items()))
print(new_dict1)


# Example 3 - Sort Dictionary By Value in Python

my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict)

print(sortedDict)


# Example 4 - sort list dict by value using ITEMGETTER

from operator import itemgetter

list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
 
print("The list printed sorting by age: ")
print(sorted(list, key=itemgetter('age')))
print("\r")

print("The list printed sorting by age and name: ")
print(sorted(list, key=itemgetter('age', 'name')))
print("\r")

          # sorted by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list, key=itemgetter('age'), reverse=True))


O/P :
{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}
{1: 2, 2: 56, 3: 323, 4: 24, 5: 12, 6: 18}
['num1', 'num2', 'num3', 'num4', 'num5', 'num6']



The list printed sorting by age: 
[{'name': 'Nikhil', 'age': 19}, {'name': 'Nandini', 'age': 20}, {'name': 'Manjeet', 'age': 20}]

The list printed sorting by age and name: 
[{'name': 'Nikhil', 'age': 19}, {'name': 'Manjeet', 'age': 20}, {'name': 'Nandini', 'age': 20}]

The list printed sorting by age in descending order: 
[{'name': 'Nandini', 'age': 20}, {'name': 'Manjeet', 'age': 20}, {'name': 'Nikhil', 'age': 19}]