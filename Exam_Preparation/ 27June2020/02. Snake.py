def is_in_range(r, c, matrix_size):
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        return True
    return False


# square matrix

size = int(input())

matrix = [[x for x in input()] for row in range(size)]

# [
# ['-', '-', '-', '-', '-', 'S'],
# ['-', '-', '-', '-', 'B', '-'],
# ['-', '-', '-', '-', '-', '-'],
# ['-', '-', '-', '-', '-', '-'],
# ['-', '-', 'B', '-', '-', '-'],
# ['-', '-', '*', '-', '-', '-']
# ]

snake_movement = {
    "up": (-1, 0),
    "down": (+1, 0),
    "right": (0, +1),
    "left": (0, -1)
}
snake_row, snake_col = None, None
burrow_coord = []
food_quantity = 0
won = True

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            snake_row, snake_col = row, col
        if matrix[row][col] == "B":
            burrow_coord.append([row, col])

command = input()
while command != "":

    next_snake_row, next_snake_col = snake_row + snake_movement[command][0], snake_col + snake_movement[command][1]
    if not is_in_range(next_snake_row, next_snake_col, size):
        matrix[snake_row][snake_col] = "."
        won = False
        break

    if matrix[next_snake_row][next_snake_col] == "-":
        matrix[snake_row][snake_col] = "."
        snake_row, snake_col = next_snake_row, next_snake_col
        matrix[snake_row][snake_col] = "S"
    elif matrix[next_snake_row][next_snake_col] == "B":
        matrix[snake_row][snake_col] = "."
        snake_row, snake_col = next_snake_row, next_snake_col
        matrix[snake_row][snake_col] = "."
        burrow_coord.remove([snake_row, snake_col])
        next_snake_row, next_snake_col = burrow_coord[0][0], burrow_coord[0][1]
        snake_row, snake_col = next_snake_row, next_snake_col
        matrix[snake_row][snake_col] = "S"
    elif matrix[next_snake_row][next_snake_col] == "*":
        food_quantity += 1
        matrix[snake_row][snake_col] = "."
        snake_row, snake_col = next_snake_row, next_snake_col
        matrix[snake_row][snake_col] = "S"
        if food_quantity >= 10:
            won = True
            break

    command = input()

if won:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food_quantity}")

[print(''.join(row)) for row in matrix]
