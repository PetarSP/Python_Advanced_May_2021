# 10:40
from collections import deque

initial_input = deque(input().split())

colors_found = []

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}


while initial_input:
    first_sub_str = initial_input.popleft()
    if initial_input:
        second_sub_str = initial_input.pop()
        concatenated_color = first_sub_str + second_sub_str
    else:
        concatenated_color = first_sub_str

    if concatenated_color in main_colors or concatenated_color in secondary_colors:
        colors_found.append(concatenated_color)

    elif ((second_sub_str + first_sub_str) in main_colors) or ((second_sub_str + first_sub_str) in secondary_colors):
        concatenated_color = second_sub_str + first_sub_str
        colors_found.append(concatenated_color)

    else:
        first_sub_str = first_sub_str[:-1]
        second_sub_str = second_sub_str[:-1]
        if len(initial_input) % 2 == 0:
            middle_index = (len(initial_input) // 2)
            if first_sub_str:
                initial_input.insert(middle_index, first_sub_str)
            if second_sub_str:
                initial_input.insert(middle_index, second_sub_str)
        else:
            middle_index = (len(initial_input) // 2)
            if first_sub_str:
                initial_input.insert(middle_index, first_sub_str)
            if second_sub_str:
                initial_input.insert(middle_index, second_sub_str)

if "orange" in colors_found:
    if not("red" in colors_found) or not ("yellow" in colors_found):
        colors_found.remove("orange")
if "purple" in colors_found:
    if not("red" in colors_found) or not("blue" in colors_found):
        colors_found.remove("purple")
if "green" in colors_found:
    if not("yellow" in colors_found) or not("blue" in colors_found):
        colors_found.remove("green")

print(colors_found)

# 11:40 break
# 11:50 resume