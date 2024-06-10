height_in_cm = int(input())

height_30_cm = height_in_cm - 30

jumps_qty = 0
fails_qty = 0

while True:
    height_entered = int(input())

    jumps_qty += 1
    if height_entered > height_30_cm:
        height_30_cm += 5
        fails_qty = 0
    elif height_entered <= height_30_cm:
        fails_qty += 1
        if fails_qty == 3:
            print(f"Tihomir failed at {height_30_cm}cm after {jumps_qty} jumps.")
            break

    if height_30_cm > height_in_cm:
        print(f"Tihomir succeeded, he jumped over {height_in_cm}cm after {jumps_qty} jumps.")
        break

