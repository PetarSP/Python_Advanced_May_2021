def read_matrix():
    n, m = [int(x) for x in input().split(", ")]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()

# columns:
# [0][1][2][3][4][5]
#  ^  ^  ^  ^  ^  ^
#  |  |  |  |  |  |
#  7  1  3  3  2  1 -> row[0]
#  1  3  9  8  5  6 -> row[1]
#  4  6  7  9  1  0 -> row[2]

n = len(matrix)
m = len(matrix[0])

column_sum = [0] * m

for r in range(n):
    for c in range(m):
        value = matrix[r][c]
        column_sum[c] += value

[print(x) for x in column_sum]