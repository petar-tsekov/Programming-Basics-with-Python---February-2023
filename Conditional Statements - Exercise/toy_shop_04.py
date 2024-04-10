
trip_price = float(input())
puzzle_qty = int(input())
talking_doll_qty = int(input())
teddy_bear_qty = int(input())
minions_qty = int(input())
truck_qty = int(input())


total_price = puzzle_qty * 2.60 + talking_doll_qty * 3 + teddy_bear_qty * 4.10 + minions_qty * 8.20 + truck_qty * 2
total_toys_qty = puzzle_qty + talking_doll_qty + teddy_bear_qty + minions_qty + truck_qty

if total_toys_qty >= 50:
    total_price =total_price - total_price * 0.25

total_price = total_price - total_price * 0.10

if total_price >= trip_price:
    total_price -= trip_price
    print(f"Yes! {total_price:.2f} lv left.")

elif total_price <= trip_price:
    trip_price -= total_price
    print(f"Not enough money! {trip_price:.2f} lv needed.")


