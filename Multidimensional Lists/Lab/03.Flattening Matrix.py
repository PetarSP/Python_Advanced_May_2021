current_list = []
last_list = []
num_of_rows = int(input())
for _ in range(num_of_rows):
    each_line = [int(x) for x in input().split(", ")]
    current_list.append(each_line)

for i in current_list:
    for j in i:
        last_list.append(j)

print(last_list)