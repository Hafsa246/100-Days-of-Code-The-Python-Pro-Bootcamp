import random

names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Dave', 'Freddie']

students_scores = {student:random.randint(1, 100) for student in names}

# new_dict = {new_key:new_value for (key, value) in old_dict.items() if test}

passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}