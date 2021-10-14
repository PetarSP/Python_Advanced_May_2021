def read_matrix():
    n, m = [int(x) for x in input().split(", ")]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]  # check this split !
        matrix.append(row)

    return matrix


# square matrix
def read_matrix():
    n = int(input())

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)

    return matrix


matrix = read_matrix()

print(matrix)

# [0][1][2][3][4][5]
#  ^  ^  ^  ^  ^  ^
#  |  |  |  |  |  |
#  7  1  3  3  2  1 -> row[0]
#  1  3  9  8  5  6 -> row[1]
#  4  6  7  9  1  0 -> row[2]


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

n = 5  # rows
# primary diagonal
print(
    [matrix[i][i] for i in range(n)]
)

# secondary diagonal
print(
    [matrix[i][n - i - 1] for i in range(n)]
)

# below primary diagonal
below_primary_diagonal = []
for n in range(n):
    for m in range(n):
        below_primary_diagonal.append(matrix[n][m])

print(below_primary_diagonal)

# below primary diagonal + primary diagonal
below_primary_and_primary_diagonal = []
for r in range(n):
    for c in range(r + 1):
        below_primary_and_primary_diagonal.append(matrix[r][c])

print(below_primary_and_primary_diagonal)

# above primary diagonal  - > row = 0....n
#                             col = row + 1 * n

# below secondary diagonal - > row = 0 ... n
#                               col = n - row .... n

# above secondary diagonal  - > row = 0 ...n
#                               col = 0 ... n - row - 2
