
groups_qty = int(input())

musala_qty = 0
monblan_qty = 0
kilimandjaro_qty = 0
k2_qty = 0
everest_qty = 0

for x in range(groups_qty):
    people_qty = int(input())

    if people_qty <= 5:
        musala_qty += people_qty

    elif 6 <= people_qty <= 12:
        monblan_qty += people_qty

    elif 13 <= people_qty <= 25:
        kilimandjaro_qty += people_qty

    elif 26 <= people_qty <= 40:
        k2_qty += people_qty

    else:
        everest_qty += people_qty

total_people = musala_qty + monblan_qty + kilimandjaro_qty + k2_qty + everest_qty

percent_musala = musala_qty / total_people * 100
percent_monblan = monblan_qty / total_people * 100
percent_kilimandjaro = kilimandjaro_qty / total_people * 100
percent_k2 = k2_qty / total_people * 100
percent_everest = everest_qty / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")

