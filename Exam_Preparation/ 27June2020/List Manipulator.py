from collections import deque


def list_manipulator(list_of_numbers: list, operation: str, beginning_or_end: str, *args):
    if operation == "add":
        assert len(args) > 0
        if beginning_or_end == "beginning":
            list_of_numbers = list(args) + list_of_numbers
            return list_of_numbers
        elif beginning_or_end == "end":
            list_of_numbers = list_of_numbers + list(args)
            return list_of_numbers

    if operation == "remove":
        assert 0 <= len(args) <= 1
        if beginning_or_end == "beginning":
            if args:
                num = int(*args)
                list_of_numbers = list_of_numbers[num:]
                return list_of_numbers
            else:
                list_of_numbers = list_of_numbers[1:]
                return list_of_numbers
        elif beginning_or_end == "end":
            if args:
                num = int(*args)
                list_of_numbers = list_of_numbers[:num - 1]
                return list_of_numbers
            else:
                list_of_numbers.pop()
                return list(list_of_numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
