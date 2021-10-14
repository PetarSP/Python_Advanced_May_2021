command = input()

numbers = [int(x) for x in input().split()]

#  Variant 1

# if command == "Odd":
#     odd = sum(filter(lambda x: x % 2 == 1, numbers)) * len(numbers)
#     print(odd)
# elif command == "Even":
#     even = sum(filter(lambda x: x % 2 == 0, numbers)) * len(numbers)
#     print(even)

# Variant 2

parity = 0 if command == "Even" else 1

filtered_sum = sum(filter(lambda x: x % 2 == parity, numbers)) * len(numbers)

print(filtered_sum)