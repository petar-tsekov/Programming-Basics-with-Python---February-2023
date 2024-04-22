
lily_age = int(input())
washing_machine_price = float(input())
toys_price = int(input())

total_sum = 0
additiponal_sum = 10
toys_count = 0

for x in range(1, lily_age + 1):
    if x % 2 == 0:
        total_sum += additiponal_sum
        additiponal_sum += 10
        total_sum -= 1

    else:
        toys_count += 1

toys_sold = toys_count * toys_price
total = toys_sold + total_sum

if total >= washing_machine_price:
    print(f"Yes! {total - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total:.2f}")

