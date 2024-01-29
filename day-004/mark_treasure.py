line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
column = position[0].lower()
row = int(position[1])

columns = ['a', 'b', 'c']
column_number = columns.index(column) # função para achar um item dentro de uma lista.
  
map[row-1][column_number] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")