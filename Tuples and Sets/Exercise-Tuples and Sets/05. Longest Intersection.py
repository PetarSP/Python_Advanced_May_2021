def interval(some_list: str):
    start, end = [int(i) for i in some_list.split(",")]
    return {i for i in range(start, end + 1)}


n = int(input())

all_intersections = []

for _ in range(n):
    first_range, second_range = input().split("-")
    first_interval = interval(first_range)
    second_interval = interval(second_range)
    current_intersection = first_interval.intersection(second_interval)
    all_intersections.append(current_intersection)

len_intersection = 0
longest_intersection_index = 0
for index in range(len(all_intersections)):
    if len(all_intersections[index]) > len_intersection :
        len_intersection = len(all_intersections[index])
        longest_intersection_index = index

print(f"Longest intersection is {list(all_intersections[longest_intersection_index])} with length {len_intersection}")