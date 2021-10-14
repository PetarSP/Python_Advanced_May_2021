def is_knight_placed(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board):
        return board[r][c] == "K"
    return False


def count_affected_knights(board, r, c):
    result = 0
    if is_knight_placed(board, r - 2, c - 1):
        result += 1
    if is_knight_placed(board, r - 2, c + 1):
        result += 1
    if is_knight_placed(board, r - 1, c - 2):
        result += 1
    if is_knight_placed(board, r - 1, c + 2):
        result += 1
    if is_knight_placed(board, r + 2, c - 1):
        result += 1
    if is_knight_placed(board, r + 2, c + 1):
        result += 1
    if is_knight_placed(board, r + 1, c - 2):
        result += 1
    if is_knight_placed(board, r + 1, c + 2):
        result += 1

    return result


size = int(input())

board = [[x for x in input()] for _ in range(size)]

# [ 0    1    2    3    4
# ['0', 'X', '0', 'X', '0'], 0
# ['X', '0', '0', '0', 'X'], 1
# ['0', '0', (2,2) , '0', '0'], 2
# ['X', '0', '0', '0', 'X'], 3
# ['0', 'X', '0', 'X', '0']  4
# ]

removed_knights = 0

while True:
    max_count, knight_row, knight_col = 0, 0, 0
    for row in range(size):
        for col in range(size):
            if board[row][col] == "0":
                continue
            count = count_affected_knights(board, row, col)
            if count > max_count:
                max_count, knight_row, knight_col = count, row, col
    if max_count == 0:
        break
    board[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)
