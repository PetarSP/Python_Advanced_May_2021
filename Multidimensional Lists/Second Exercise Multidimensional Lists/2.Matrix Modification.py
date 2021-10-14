def is_position_valid(r, c, size):
    return 0 <= r < size and 0 <= c < size


size = int(input())

matrix = [[int(x) for x in input().split()] for x in range(size)]

command = input()

while not command == "END":
    action = command.split()[0]
    row, col, value = map(int,command.split()[1:])
    if not is_position_valid(row, col, size):
        print("Invalid coordinates")
        command = input()
        continue
    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value
    command = input()

for x in matrix:
    print(" ".join([str(x) for x in x]))
