from collections import deque

num_petrol_stations = int(input())

list_of_stations = deque()

for _ in range(num_petrol_stations):
    pump = [int(x) for x in input().split()]
    list_of_stations.append(pump)

for idx in range(num_petrol_stations):
    car_fuel = 0
    completed = True
    for petrol, distance in list_of_stations:
        car_fuel += petrol
        if distance > car_fuel:
            completed = False
            break
        else:
            car_fuel -= distance
    if completed:
        print(idx)
        break
    list_of_stations.append(list_of_stations.popleft())