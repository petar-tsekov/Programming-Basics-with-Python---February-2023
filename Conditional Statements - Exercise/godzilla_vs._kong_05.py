
film_budget = float(input())
people_qty = int(input())
people_cloths_price = float(input())

decor_price = film_budget * 0.10
clothes_total_price = people_qty * people_cloths_price

if people_qty > 150:
    discount_from_price = clothes_total_price * 0.10
    clothes_total_price = clothes_total_price - discount_from_price

total_film_price = decor_price + clothes_total_price

if total_film_price > film_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_film_price - film_budget:.2f} leva more.")

elif total_film_price <= film_budget:
    print(f"Action!")
    print(f"Wingard starts filming with {film_budget - total_film_price:.2f} leva left.")