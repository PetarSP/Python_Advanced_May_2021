# Have to use queue

### George Peter William Paid Michael Oscar Olivia Linda End

from collections import deque

command = input()

queue = deque()

while not command == "End":
    if command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        customer_name = command
        queue.append(customer_name)

    command = input()

print(f"{len(queue)} people remaining.")
