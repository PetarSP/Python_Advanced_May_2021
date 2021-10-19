import math


# square_matrix
def is_in_range(r, c, matrix_size):
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        return True
    return False


size = int(input())

matrix = [[int(col) if col.isdigit() else col for col in input().split()] for row in range(size)]

#   0     1    2    3    4
# [ 1,   'X',  7,   9,  11],       0
# ['X',  14,  46,  62,   0],       1
# [15,   33,  21,  95,  'X'],      2
# ['P',  14,   3,   4,  18],       3
# [ 9,   20,  33,  'X',  0]        4
player_row, player_col = None, None

player_movements = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}
won = True
coins = 0
player_path = []

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            player_row, player_col = row, col

while True:
    command = input()
    if command not in player_movements:
        continue

    next_row, next_col = player_row + player_movements[command][0], player_col + player_movements[command][1]
    # going outside of the field
    if not is_in_range(next_row, next_col, size) or matrix[next_row][next_col] == "X":
        coins = coins - (50*coins / 100)
        won = False
        break
    else:
        coins += matrix[next_row][next_col]
        player_path.append([next_row, next_col])
    if coins > 100:
        won = True
        break
    player_row, player_col = next_row, next_col
if won:
    print(f"You won! You've collected {math.floor(coins)} coins.")
else:
    print(f"Game over! You've collected {math.floor(coins)} coins.")
print(f"Your path:")
for i in player_path:
    print(i)