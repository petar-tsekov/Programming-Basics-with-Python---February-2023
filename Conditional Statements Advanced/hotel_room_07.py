
month_entered = input()
stays_qty = int(input())


studio_price_for_day = 0
apartament_price_for_day = 0
total_for_studio = 0
total_for_apartament = 0

if month_entered =="May" or month_entered == "October":
    studio_price_for_day = 50
    apartament_price_for_day = 65

    if 7 < stays_qty <= 14:
        studio_price_for_day = studio_price_for_day - studio_price_for_day * 0.05
    else:
        studio_price_for_day = studio_price_for_day - studio_price_for_day * 0.30
        apartament_price_for_day = apartament_price_for_day - apartament_price_for_day * 0.10

    total_for_studio = studio_price_for_day * stays_qty
    total_for_apartament = apartament_price_for_day * stays_qty

elif month_entered == "June" or month_entered == "September":
    studio_price_for_day = 75.20
    apartament_price_for_day = 68.70

    if stays_qty > 14:
        studio_price_for_day = studio_price_for_day - studio_price_for_day * 0.20
        apartament_price_for_day = apartament_price_for_day - apartament_price_for_day * 0.10

    total_for_studio = studio_price_for_day * stays_qty
    total_for_apartament = apartament_price_for_day * stays_qty


elif month_entered == "July" or month_entered == "August":
    studio_price_for_day = 76
    apartament_price_for_day = 77

    if stays_qty > 14:
        apartament_price_for_day = apartament_price_for_day - apartament_price_for_day * 0.10

    total_for_studio = studio_price_for_day * stays_qty
    total_for_apartament = apartament_price_for_day * stays_qty

print(f"Apartment: {total_for_apartament:.2f} lv.")
print(f"Studio: {total_for_studio:.2f} lv.")



