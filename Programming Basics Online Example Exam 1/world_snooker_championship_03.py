stage = input()
ticket_model = input()
ticket_qty = int(input())
trophy_picture = input()

total_ticket_price = 0
trophy_picture_price = 0

if stage == "Quarter final":
    if ticket_model == "Standard":
        total_ticket_price = 55.50 * ticket_qty
    elif ticket_model == "Premium":
        total_ticket_price = 105.20 * ticket_qty
    elif ticket_model == "VIP":
        total_ticket_price = 118.90 * ticket_qty

elif stage == "Semi final":
    if ticket_model == "Standard":
        total_ticket_price = 75.80 * ticket_qty
    elif ticket_model == "Premium":
        total_ticket_price = 125.22 * ticket_qty
    elif ticket_model == "VIP":
        total_ticket_price = 300.40 * ticket_qty

elif stage == "Final":
    if ticket_model == "Standard":
        total_ticket_price = 110.10 * ticket_qty
    elif ticket_model == "Premium":
        total_ticket_price = 160.66 * ticket_qty
    elif ticket_model == "VIP":
        total_ticket_price = 400 * ticket_qty

if trophy_picture == 'Y':
    trophy_picture_price = ticket_qty * 40
    if total_ticket_price > 4000:
        trophy_picture_price = 0
if trophy_picture == 'N':
    ticket_qty = 0


if 2500 < total_ticket_price <= 4000:
    total_ticket_price = total_ticket_price - total_ticket_price * 0.10
elif total_ticket_price > 4000:
    total_ticket_price = total_ticket_price - total_ticket_price * 0.25

total_ticket_price = total_ticket_price + trophy_picture_price

print(f"{total_ticket_price:.2f}")
