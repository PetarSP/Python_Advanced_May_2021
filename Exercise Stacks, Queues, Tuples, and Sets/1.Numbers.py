first_sequence = {int(x) for x in input().split()}
second_sequence = {int(y) for y in input().split()}

num_of_commands = int(input())

for _ in range(num_of_commands):
    instruction = input().split()
    command = f"{instruction[0]} {instruction[1]}"
    numbers = {int(x) for x in instruction[2:]}

    if command == "Add First":
        first_sequence = first_sequence.union(numbers)

    elif command == "Add Second":
        second_sequence = second_sequence.union(numbers)

    elif command == "Remove First":
        first_sequence = first_sequence.difference(numbers)
    elif command == "Remove Second":
        second_sequence = second_sequence.difference(numbers)

    elif command == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(", ".join(str(x) for x in sorted(first_sequence)))
print(", ".join(str(y) for y in sorted(second_sequence)))
