# 15:40 - 16:40
from collections import deque

bomb_effect = deque([int(x) for x in input().split(", ")])
bomb_casing = [int(x) for x in input().split(", ")]

bomb_dict = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

bomb_created = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
bomb_pouch = False
while True:
    if bomb_created["Datura Bombs"] >= 3 and bomb_created["Cherry Bombs"] >= 3 and bomb_created[
        "Smoke Decoy Bombs"] >= 3:
        bomb_pouch = True
        break
    if not bomb_effect:
        break
    if not bomb_casing:
        break

    first_bomb_effect = bomb_effect.popleft()
    last_bomb_casing = bomb_casing.pop()
    current_bomb_sum = first_bomb_effect + last_bomb_casing

    if current_bomb_sum in bomb_dict:
        if bomb_dict[current_bomb_sum] in bomb_created:
            bomb_created[bomb_dict[current_bomb_sum]] += 1

    else:
        bomb_effect.appendleft(first_bomb_effect)
        last_bomb_casing -= 5
        bomb_casing.append(last_bomb_casing)




if bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effect])}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")
else:
    print("Bomb Casings: empty")

for key, value in sorted(bomb_created.items()):
    print(f"{key}: {value}")


# def is_bomb_pouch_full(bomb_created):
#   return all([el >= 3 for el in bomb_created.values()])