from collections import deque

water_quantity = int(input())
name = input()
queue = deque()

while not name == "Start":
    queue.append(name)
    name = input()

command = input()

while not command == "End":
    command = command.split()
    if command[0] == "refill":
        water_quantity += int(command[1])
        command = input()
    else:
        current_person = queue.popleft()
        water_spend = int(command[0])
        if water_quantity >= water_spend:
            water_quantity -= water_spend
            print(f"{current_person} got water")
            command = input()
        else:
            print(f"{current_person} must wait")
            command = input()
print(f"{water_quantity} liters left")