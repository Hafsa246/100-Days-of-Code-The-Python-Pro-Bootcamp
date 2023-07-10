# find the sum of all items in a dictionary
dict = {'a': 100, 'b': 200, 'c': 300}

Sum = 0

for i in dict:
    Sum += dict[i]

    # or

def returnSum(dict):
    return sum(dict.values())

print(Sum)
print(returnSum(dict))