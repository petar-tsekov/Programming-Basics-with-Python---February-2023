
group_budget = int(input())
season_entered = input()
fisherman_qty = int(input())

ship_rent = 0
final_price = 0

if season_entered == "Spring":
    ship_rent = 3000
elif season_entered == "Summer" or season_entered == "Autumn":
    ship_rent = 4200
elif season_entered == "Winter":
    ship_rent = 2600

if fisherman_qty <= 6:
    final_price = ship_rent - ship_rent * 0.10
elif 7 < fisherman_qty <=11:
    final_price = ship_rent - ship_rent * 0.15
else:
    final_price = ship_rent - ship_rent * 0.25

if fisherman_qty % 2 == 0 and season_entered != "Autumn":
    final_price = final_price - final_price * 0.05

if final_price <= group_budget:
    remaining_money = final_price - group_budget
    print(f"Yes! You have {abs(remaining_money):.2f} leva left.")
else:
    needed_money = group_budget - final_price
    print(f"Not enough money! You need {abs(needed_money):.2f} leva.")