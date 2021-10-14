# 1700:1715

from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

fireworks_created = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
show = False
while True:

    if all([x >= 3 for x in fireworks_created.values()]):
        show = True
        break
    if not firework_effects:
        break
    if not explosive_power:
        break

    first_firework_effect = firework_effects.popleft()
    last_explosive_power = explosive_power.pop()
    sum_fire_exp = first_firework_effect + last_explosive_power

    if first_firework_effect <= 0 and last_explosive_power <= 0:
        continue

    if first_firework_effect <= 0:
        explosive_power.append(last_explosive_power)
        continue

    if last_explosive_power <= 0:
        firework_effects.appendleft(first_firework_effect)
        continue
    if sum_fire_exp % 3 == 0 and not sum_fire_exp % 5 == 0:
        if "Palm Fireworks" not in fireworks_created:
            fireworks_created["Palm Fireworks"] = 1
        else:
            fireworks_created["Palm Fireworks"] += 1
    elif sum_fire_exp % 5 == 0 and not sum_fire_exp % 3 == 0:
        if "Willow Fireworks" not in fireworks_created:
            fireworks_created["Willow Fireworks"] = 1
        else:
            fireworks_created["Willow Fireworks"] += 1
    elif sum_fire_exp % 5 == 0 and sum_fire_exp % 3 == 0:
        if "Crossette Fireworks" not in fireworks_created:
            fireworks_created["Crossette Fireworks"] = 1
        else:
            fireworks_created["Crossette Fireworks"] += 1
    else:
        first_firework_effect -= 1
        firework_effects.append(first_firework_effect)
        explosive_power.append(last_explosive_power)

if show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for key, value in fireworks_created.items():
    print(f"{key}: {value}")
