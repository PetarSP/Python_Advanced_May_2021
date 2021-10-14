count_of_input = int(input())

periodic_table = set()

for _ in range(count_of_input):
    command = input().split()
    for el in command:
        periodic_table.add(el)

[print(x) for x in periodic_table]