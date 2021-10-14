def valid_bunny_path(size, row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


size = int(input())

# field = [[x if not x.isdigit() else int(x) for x in input().split()] for _ in range(size)]
#

# for row in range(size):
#     for col in range(size):
#         if field[row][col] == "B":
#             bunny_row, bunny_col = row, col
field = []
bunny_row, bunny_col = 0, 0
for row in range(size):
    elements = input().split()
    field.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "B":
            bunny_row, bunny_col = row, col
max_collected_eggs = float("-inf")
max_collected_eggs_path = []
valid_direction = ""
directions = {
    # moving upwards
    "up": lambda r, c: (r - 1, c),
    # moving downwards
    "down": lambda r, c: (r + 1, c),
    # moving right
    "right": lambda r, c: (r, c + 1),
    # moving left
    "left": lambda r, c: (r, c - 1)
}

for direction, step in directions.items():
    collected_eggs = 0
    path = []
    current_row, current_col = bunny_row, bunny_col
    while True:
        current_row, current_col = step(current_row, current_col)
        if not valid_bunny_path(size, current_row, current_col):
            break
        if field[current_row][current_col] == "X":
            break
        collected_eggs += int(field[current_row][current_col])
        path.append([current_row, current_col])
        if collected_eggs > max_collected_eggs:
            max_collected_eggs, max_collected_eggs_path, valid_direction = collected_eggs, path, direction

print(valid_direction)
for x in max_collected_eggs_path:
    print(x)
print(max_collected_eggs)
