from collections import deque


def best_list_pureness(list_of_numbers: list, k: int):
    pureness = {}
    max_pureness_coord = {0: ''}
    current_pureness = 0
    list_of_numbers = deque(list_of_numbers)
    for turn in range(k + 1):
        for num in list_of_numbers:
            current_pureness += num * list_of_numbers.index(num)
        pureness[turn] = current_pureness
        current_pureness = 0
        last_element = list_of_numbers.pop()
        list_of_numbers.appendleft(last_element)
    all_dict_values = pureness.values()
    max_value = max(all_dict_values)
    for value, key in pureness.items():
        if key == max_value:
            return f"Best pureness {key} after {value} rotations"



test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


