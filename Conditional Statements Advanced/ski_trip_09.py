
stays_qty = int(input())
room_type = input()
review = input()

nights_total = stays_qty - 1
room_price = 18
apartament_price = 25
presidentt_apartament_price = 35
total_price = 0

if room_type == "room for one person":
    total_price = room_price * nights_total

elif room_type == "apartment":
    total_price = apartament_price * nights_total
    if nights_total < 10:
        total_price = total_price - total_price * 0.30
    elif 10 <= nights_total <= 15:
        total_price = total_price - total_price * 0.35
    else:
        total_price = total_price - total_price * 0.50

elif room_type == "president apartment":
    total_price = presidentt_apartament_price * nights_total
    if nights_total < 10:
        total_price = total_price - total_price * 0.10
    elif 10 <= nights_total <= 15:
        total_price = total_price - total_price * 0.15
    else:
        total_price = total_price - total_price * 0.20

if review == "positive":
    total_price = total_price + total_price * 0.25
elif review == "negative":
    total_price = total_price - total_price * 0.10

print(f"{total_price:.2f}")
