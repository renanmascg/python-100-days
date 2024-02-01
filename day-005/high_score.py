# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_number = student_scores[0]

for n in student_scores:
  if n > max_number:
    max_number = n

print(f'The highest score in the class is: {max_number}')