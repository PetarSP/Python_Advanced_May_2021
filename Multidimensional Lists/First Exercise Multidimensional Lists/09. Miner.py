# 1310

from collections import deque


def is_in_range(r, c, matrix_size):
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        return True
    return False


# square_matrix

size = int(input())
commands_for_movement_of_miner = deque(input().split())
matrix = [[x for x in input().split()] for rows in range(size)]

# [
# ['*', '*', '*', 'c', '*'],
# ['*', '*', '*', 'e', '*'],
# ['*', '*', 'c', '*', '*'],
# ['s', '*', '*', 'c', '*'],
# ['*', '*', 'c', '*', '*']
# ]

miner_path = {
    "up": (-1, 0),
    "down": (+1, 0),
    "right": (0, +1),
    "left": (0, -1)
}

miner_row, miner_col = None, None
coal_found = 0
total_coal = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "s":
            miner_row, miner_col = row, col
        if matrix[row][col] == "c":
            total_coal += 1

while commands_for_movement_of_miner:
    if commands_for_movement_of_miner:
        current_command = commands_for_movement_of_miner.popleft()

        next_row, next_col = miner_row + miner_path[current_command][0], miner_col + miner_path[current_command][1]

        if not is_in_range(next_row, next_col, size):
            continue

        elif matrix[next_row][next_col] == "e":
            print(f"Game over! ({next_row}, {next_col})")
            quit()

        elif matrix[next_row][next_col] == "c":
            coal_found += 1
            matrix[next_row][next_col] = "*"

        miner_row, miner_col = next_row, next_col

if (total_coal - coal_found) == 0:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
else:
    print(f"{total_coal - coal_found} pieces of coal left. ({miner_row}, {miner_col})")
