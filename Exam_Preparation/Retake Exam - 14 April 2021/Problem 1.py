# 1200:1220
# 1230: 1236
# total 26 minutes
from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees_capacity = [int(x) for x in input().split(", ")]
order_done = False

total_pizzas_made = 0
while True:

    if not pizza_orders:
        print(f"All orders are successfully completed!")
        print(f"Total pizzas made: {total_pizzas_made}")
        print(f"Employees: {', '.join([str(x) for x in employees_capacity])}")
        break

    first_pizza_order = pizza_orders.popleft()
    last_employee_capacity = employees_capacity.pop()

    if first_pizza_order <= 0:
        employees_capacity.append(last_employee_capacity)
        continue

    if first_pizza_order > 10:
        employees_capacity.append(last_employee_capacity)
        continue

    if first_pizza_order <= last_employee_capacity:
        order_done = True
        total_pizzas_made += first_pizza_order
        continue

    elif first_pizza_order > last_employee_capacity:
        remaining_pizza_order = first_pizza_order - last_employee_capacity
        total_pizzas_made += last_employee_capacity
        pizza_orders.appendleft(remaining_pizza_order)
        if not employees_capacity:
            order_done = False
            break
        continue

if not employees_capacity and pizza_orders:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")



