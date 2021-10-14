from collections import deque

food_quantity = int(input())
orders = [int(order) for order in input().split()]
# keep the orders in a queue
orders_as_deque = deque(orders)
print(max(orders))

while orders_as_deque:
    if (food_quantity - orders_as_deque[0]) < 0:
        break
    else:
        food_quantity -= orders_as_deque[0]
        orders_as_deque.popleft()

if not orders_as_deque:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(order) for order in orders_as_deque])}")
    # print(f"Orders left: {' '.join(map(str, orders_as_deque))}")