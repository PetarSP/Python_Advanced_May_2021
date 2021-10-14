size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][size - i - 1] for i in range(len(matrix))]

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)
