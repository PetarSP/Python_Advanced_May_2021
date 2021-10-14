def read_matrix():
    n = int(input())

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)

    return matrix


matrix = read_matrix()

# matrix = [
#     [11, 2, 4],
#     [4, 5, 6],
#     [10, 8, -12]
# ]

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
print(sum(primary_diagonal))