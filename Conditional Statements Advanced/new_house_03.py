
flower_type = input()
flower_qty = int(input())
total_budget = int(input())

flower_price = 0

if flower_type == "Roses":
    flower_price = flower_qty * 5
    if flower_qty > 80:
        flower_price = flower_price - flower_price * 0.10
elif flower_type == "Dahlias":
    flower_price = flower_qty * 3.80
    if flower_qty > 90:
        flower_price = flower_price - flower_price * 0.15
elif flower_type == "Tulips":
    flower_price = flower_qty * 2.80
    if flower_qty > 80:
        flower_price = flower_price - flower_price * 0.15
elif flower_type == "Narcissus":
    flower_price = flower_qty * 3
    if flower_qty < 120:
        flower_price = flower_price + flower_price * 0.15
elif flower_type == "Gladiolus":
    flower_price = flower_qty * 2.50
    if flower_qty < 80:
        flower_price = flower_price + flower_price * 0.20

if total_budget >= flower_price:
    print(f"Hey, you have a great garden with {flower_qty} {flower_type} and {total_budget - flower_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {flower_price - total_budget:.2f} leva more.")





