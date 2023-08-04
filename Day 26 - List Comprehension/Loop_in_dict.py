import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries

# for (key, value) in student_dict.items():
#     print(value)


student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a Dataframe
# for (key, value) in student_data_frame.items():
#     print(value)


# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.score)


