total_months = int(input())

total_electricity_bill = 0
total_water_bill = 0
water_bill = 20
total_internet_bill = 0
internet_bill = 15
total_other_bill = 0
other_bill = 0
average_bill = 0

for month in range(total_months):
    electricity_bill = float(input())
    total_electricity_bill += electricity_bill
    total_water_bill += 20
    total_internet_bill += 15
    other_bill = (electricity_bill + water_bill + internet_bill) + (electricity_bill + water_bill + internet_bill) * 0.20
    total_other_bill += other_bill
average_bill = (total_electricity_bill + total_water_bill + total_internet_bill + total_other_bill) / total_months

print(f"Electricity: {total_electricity_bill:.2f} lv")
print(f"Water: {total_water_bill:.2f} lv")
print(f"Internet: {total_internet_bill:.2f} lv")
print(f"Other: {total_other_bill:.2f} lv")
print(f"Average: {average_bill:.2f} lv")