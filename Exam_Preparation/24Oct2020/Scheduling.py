# 14:00

from collections import deque

jobs = [int(x) for x in input().split(", ")]
interested_job_index = int(input())

total_clock_cycles = 0
wanted_job = jobs[interested_job_index]

initial_jobs_indices = []

for idx in range(len(jobs)):
    current_job, index = jobs[idx], idx
    initial_jobs_indices.append([current_job, index])

sorted_jobs = deque(sorted(initial_jobs_indices, key=lambda x: x[0]))

# [[1, 1], [1, 3], [2, 4], [3, 0], [10, 2]]

while True:
    current_num, current_num_idx = sorted_jobs.popleft()

    if current_num_idx == interested_job_index:
        total_clock_cycles+=current_num
        break
    total_clock_cycles += current_num

print(total_clock_cycles)