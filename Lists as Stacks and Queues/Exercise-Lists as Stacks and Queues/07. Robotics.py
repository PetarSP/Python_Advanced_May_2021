from collections import deque
from math import floor


class Robot:
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.busy_until = 0


def get_time_in_seconds(time):
    hours, minutes, seconds = [int(x) for x in time.split(":")]
    return hours * 60 * 60 + minutes * 60 + seconds


def get_time_from_seconds(seconds):
    seconds %= (24 * 60 * 60)
    hours = floor(seconds // (60 * 60))
    minutes = floor((seconds / 60) % 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots = []

robots_input = input().split(";")
for robot in robots_input:
    name, processing_time = robot.split("-")
    robots.append(Robot(name, int(processing_time)))

time_in_seconds = get_time_in_seconds(input())

items = deque()

while True:
    product = input()
    if product == "End":
        break
    items.append(product)

while items:
    current_item = items.popleft()
    time_in_seconds += 1
    found_robot = False

    for robot in robots:
        if time_in_seconds >= robot.busy_until:
            robot.busy_until = time_in_seconds + robot.processing_time
            found_robot = True
            print(f"{robot.name} - {current_item} [{get_time_from_seconds(time_in_seconds)}]")
            break

    if not found_robot:
        items.append(current_item)
