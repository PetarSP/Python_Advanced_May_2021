from collections import deque
from math import floor


# First version


def minus(queue: list):
    result = queue[0]
    for el_index in range(1, len(queue) - 1):
        result -= queue[el_index]
    return result


def multiply(queue: list):
    result = queue[0]
    for el_index in range(1, len(queue) - 1):
        result *= queue[el_index]
    return result


def divide(queue: list):
    result = queue[0]
    for el_index in range(1, len(queue) - 1):
        result /= queue[el_index]
    return floor(result)


# Second version

# algorithmic_expressions = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a // b
# }

expression = deque(int(x) if x not in "*/+-" else x for x in input().split())

queue = []

while expression:
    el = expression.popleft()
    queue.append(el)
    if el == "+":
        queue = [sum(queue[:-1])]
    elif el == "-":
        queue = [minus(queue)]
    elif el == "*":
        queue = [multiply(queue)]
    elif el == "/":
        queue = [divide(queue)]

print(queue[0])
