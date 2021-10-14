from collections import deque

box_of_clothes = deque(map(int, input().split(" ")))
rack_capacity = int(input())

current_rack = 0
num_of_racks_used = 0
while box_of_clothes:
    current_stack_of_clothes = box_of_clothes.pop()
    current_rack += current_stack_of_clothes

    if current_rack == rack_capacity:
        num_of_racks_used += 1
        current_rack = 0
    if current_rack > rack_capacity:
        clothes_left = current_stack_of_clothes
        box_of_clothes.append(clothes_left)
        num_of_racks_used += 1
        current_rack = 0
if current_rack:
    num_of_racks_used += 1

print(num_of_racks_used)
