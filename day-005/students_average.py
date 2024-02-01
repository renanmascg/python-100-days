# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
number_of_students = 0
sum_of_heights = 0

for height in student_heights:
  number_of_students += 1
  sum_of_heights += height

average_height = round(sum_of_heights/number_of_students)

print(f'total height = {sum_of_heights}')
print(f'number of students = {number_of_students}')
print(f'average height = {average_height}')