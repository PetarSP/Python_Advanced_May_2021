from collections import deque


def current_collected_honey(bee, symbol, nectar):
    collected_honey = 0
    if symbol == "+":
        collected_honey = abs(bee + nectar)
    elif symbol == "-":
        collected_honey = abs(bee - nectar)
    elif symbol == "*":
        collected_honey = abs(bee * nectar)
    elif symbol == "/":
        if nectar > 0:
            collected_honey = abs(bee / nectar)
    return collected_honey


working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey_made = 0

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        symbol = symbols.popleft()
        honey_made = current_collected_honey(current_bee, symbol, current_nectar)
        total_honey_made += honey_made
    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {total_honey_made}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
