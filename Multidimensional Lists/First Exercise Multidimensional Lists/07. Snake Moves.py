from collections import deque

rows, cols = [int(x) for x in input().split()]

matrix = [deque(["" for x in range(cols)]) for _ in range(rows)]

snake = deque(input())

# [
# ['S', 'o', 'f', 't', 'U', 'n'],
# ['U', 't', 'f', 'o', 'S', 'i'],
# ['', '', '', '', '', ''],
# ['', '', '', '', '', ''],
# ['', '', '', '', '', '']
# ]
# deque(['S', 'o', 'f', 't', 'U', 'n', 'i'])

for r in range(rows):
    if r % 2 == 0 or r == 0:
        for c in range(cols):
            first_el = snake.popleft()
            matrix[r][c] = first_el
            snake.append(first_el)
    if r % 2 == 1:
        for c in range(1, cols + 1):
            first_el = snake.popleft()
            matrix[r][-c] = first_el
            snake.append(first_el)

for r in range(len(matrix)):
    print("".join(matrix[r]))
