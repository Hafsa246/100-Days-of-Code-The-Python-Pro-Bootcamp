# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum1 = 0
for i in range(0, len(student_heights)):
    sum1 += student_heights[i]

sum2 = sum1/len(student_heights)
print(round(sum2))

