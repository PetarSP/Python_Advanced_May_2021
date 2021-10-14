# 1810- 1831

from collections import deque

customers = deque([int(x) for x in input().split(", ")])  # time to drive to the destination
taxis = deque([int(x) for x in input().split(", ")])  # time to drive bfr need to refill

total_time_passed = 0

while True:

    if not taxis:
        break

    if not customers:
        break

    first_customer = customers.popleft()
    last_taxi = taxis.pop()

    #   the taxi can drive the customer

    if last_taxi >= first_customer:
        total_time_passed += first_customer

    #   the taxi cant drive the customer

    if last_taxi < first_customer:
        customers.appendleft(first_customer)

if not customers:
    print(f"All customers were driven to their destinations ")
    print(f"Total time: {total_time_passed} minutes")
if customers and not taxis:
    print(f"Not all customers were driven to their destinations ")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
