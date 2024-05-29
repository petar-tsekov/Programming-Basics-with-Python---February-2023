import math

tennis_rocket_price = int(input())
tennis_rocket_qty = int(input())
shoes_qty = int(input())

rocket_price_total = tennis_rocket_price * tennis_rocket_qty
shoes_price = tennis_rocket_price / 6
shoes_price_total = shoes_price * shoes_qty
equipment_price_total = (rocket_price_total + shoes_price_total) * 0.20
total_price = rocket_price_total + shoes_price_total + equipment_price_total

print(f"Price to be paid by Djokovic {math.floor(total_price/8)}")
print(f"Price to be paid by sponsors {math.ceil(total_price * 7/8)}")