n = int(input())

primary_diagonal = []
secondary_diagonal = []

matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
n = len(matrix)
m = len(matrix[0])

primary_diagonal = [matrix[i][i] for i in range(n)]

secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]


print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

