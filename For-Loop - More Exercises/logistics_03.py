cargo_qty = int(input())

total_weight = 0
percent_weight = 0
van_weight = 0
truck_weight = 0
train_weight = 0

for cargo in range(cargo_qty):
    cargo_weight = int(input())
    total_weight += cargo_weight

    if cargo_weight <= 3:
        van_weight += cargo_weight
    elif 4 <= cargo_weight <= 11:
        truck_weight += cargo_weight
    else:
        train_weight += cargo_weight

percent_weight = (van_weight * 200 + truck_weight * 175 + train_weight * 120)/total_weight
print(f"{percent_weight:.2f}")
print(f"{van_weight/total_weight * 100:.2f}%")
print(f"{truck_weight/total_weight * 100:.2f}%")
print(f"{train_weight/total_weight * 100:.2f}%")
