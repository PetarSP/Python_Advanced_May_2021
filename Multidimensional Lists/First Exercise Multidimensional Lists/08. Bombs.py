def is_in_range(r, c, matrix_size, matrix):
    if 0 <= r < matrix_size and 0 <= c < matrix_size and matrix[r][c] > 0:
        return True
    return False


bomb_path = {
    "up": (- 1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1),
    "up_right": (- 1, 1),
    "up_left": (- 1, - 1),
    "down_right": (1, 1),
    "down_left": (1, - 1)
}

# square matrix
size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

# [
# ['8', '3', '2', '5'],
# ['6', '4', '7', '9'],
# ['9', '9', '3', '6'],
# ['6', '8', '1', '2']
# ]

bomb_indices = [[int(idx) for idx in x.split(",")] for x in input().split()]
bomb_power_list = []

# [[1, 2], [2, 1], [2, 0]]

for indices in bomb_indices:
    row, col = indices
    if matrix[row][col] <= 0:
        continue
    for direction in bomb_path:
        next_row, next_col = bomb_path[direction]
        bomb_row, bomb_col = row + next_row, col + next_col
        if is_in_range(bomb_row, bomb_col, size, matrix):
            matrix[bomb_row][bomb_col] -= matrix[row][col]

    matrix[row][col] = 0

alive_cells = []

for r in range(size):
    for c in range(size):
        if matrix[r][c] > 0:
            alive_cells.append(matrix[r][c])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    print(' '.join([str(x) for x in row]))
