# 1515 : 1551
# 36 mins

from collections import deque

males = [int(x) for x in input().split(" ")]
females = deque([int(x) for x in input().split(" ")])

total_matches = 0
while True:

    if not males:
        break
    if not females:
        break

    first_female = females.popleft()
    last_male = males.pop()

    if first_female <= 0 and last_male <= 0:
        continue
    if first_female <= 0:
        males.append(last_male)
        continue
    if last_male <= 0:
        females.appendleft(first_female)
        continue

    if first_female % 25 == 0 and last_male % 25 == 0:
        females.popleft()
        males.pop()
        continue

    if first_female % 25 == 0:
        if females:
            females.popleft()
            males.append(last_male)
        continue

    if last_male % 25 == 0:
        if males:
            males.pop()
            females.appendleft(first_female)
        continue

    if first_female == last_male:
        total_matches += 1
    else:
        last_male -= 2
        males.append(last_male)

print(f"Matches: {total_matches}")

if not males:
    print(f"Males left: none")
else:
    print(f"Males left: {', '.join(reversed([str(x) for x in males]))}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(str(x) for x in females)}")
