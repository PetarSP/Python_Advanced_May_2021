def is_in_range(size, r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def get_next_psn(direction, r, c, step=1):
    if direction == "up":
        return r - step, c
    if direction == "down":
        return r + step, c
    if direction == "right":
        return r, c + step
    if direction == "left":
        return r, c - step


size = 5

matrix = []

total_targets_on_the_field = 0
hit_targets = []
player_row, player_col = 0, 0

for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "A":
            player_row, player_col = row, col
        elif element == "x":
            total_targets_on_the_field += 1

num_commands = int(input())

for _ in range(num_commands):
    line_args = input().split()
    command, direction = line_args[0], line_args[1]

    if command == "move":
        steps = int(line_args[2])
        next_row, next_col = get_next_psn(direction, player_row, player_col, steps)
        if not is_in_range(size, next_row, next_col):
            continue
        if matrix[next_row][next_col] != ".":
            continue

        matrix[player_row][player_col] = "."
        matrix[next_row][next_col] = "A"
        player_row, player_col = next_row, next_col
    else:
        bullet_row, bullet_col = get_next_psn(direction, player_row, player_col, 1)
        while True:
            if not is_in_range(size, bullet_row, bullet_col):
                break
            if matrix[bullet_row][bullet_col] == "x":
                hit_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = "."
                break
            bullet_row, bullet_col = get_next_psn(direction, bullet_row, bullet_col, 1)
        if len(hit_targets) == total_targets_on_the_field:
            break

if len(hit_targets) == total_targets_on_the_field:
    print(f"Training completed! All {total_targets_on_the_field} targets hit.")
else:
    print(f"Training not completed! {total_targets_on_the_field - len(hit_targets)} targets left.")

for target in hit_targets:
    print(target)

# TODO: 81/100 in Judge - > do it again !!!