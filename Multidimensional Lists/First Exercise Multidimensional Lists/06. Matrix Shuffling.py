def is_valid_position(r, c, rows, cols):
    if r < 0 or c < 0 or r > rows or c > cols:
        return False
    return True


rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

while True:
    line = input()
    if line == "END":
        break

    args = line.split()
    if args[0] != "swap" or len(args) != 5:
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = [int(x) for x in args[1:]]
    if not is_valid_position(row1, col1, rows, cols) or not is_valid_position(row2, col2, rows, cols):
        print("Invalid input!")
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row_element in matrix:
        print(" ".join([str(x) for x in row_element]))