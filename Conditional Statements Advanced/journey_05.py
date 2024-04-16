
budget = float(input())
season = input()

remaining_money = 0
destination = ""
camp = ""

if budget <= 100:
    destination ="Bulgaria"
    if season == "summer":
        camp = "Camp"
        remaining_money = budget * 0.30
    elif season == "winter":
        camp ="Hotel"
        remaining_money = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        camp = "Camp"
        remaining_money = budget * 0.40
    elif season == "winter":
        camp = "Hotel"
        remaining_money = budget * 0.80
else:
    destination = "Europe"
    camp = "Hotel"
    remaining_money = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{camp} - {remaining_money:.2f}")

