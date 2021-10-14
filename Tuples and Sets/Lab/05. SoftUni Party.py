# regular_guests
# vip_guests

# when guest comes check if exists in any of the two guest list_of_numbers

num_guests = int(input())

planned_guests = set()

for guests in range(num_guests):
    reservation_code = input()
    if len(reservation_code) == 8:
        planned_guests.add(reservation_code)
while True:
    reservation_code = input()
    if reservation_code == "END":
        break
    if len(reservation_code) == 8:
        if reservation_code in planned_guests:
            planned_guests.remove(reservation_code)

print(len(planned_guests))
[print(i) for i in sorted(planned_guests)]