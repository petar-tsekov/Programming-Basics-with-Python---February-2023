stadium_capacity = int(input())
fans_qty = int(input())

sector_a = 0
sector_b = 0
sector_c = 0
sector_d = 0
percent_capacity = 0

for fans in range(fans_qty):
    fan_sector = input()

    if fan_sector =="A":
        sector_a += 1
    elif fan_sector =="B":
        sector_b += 1
    elif fan_sector =="V":
        sector_c += 1
    elif fan_sector =="G":
        sector_d += 1
print(f"{sector_a/fans_qty * 100:.2f}%")
print(f"{sector_b/fans_qty * 100:.2f}%")
print(f"{sector_c/fans_qty * 100:.2f}%")
print(f"{sector_d/fans_qty * 100:.2f}%")
print(f"{fans_qty/stadium_capacity * 100:.2f}%")



