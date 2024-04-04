
pen_count = int(input())
markers_count = int(input())
liquid_liters = int(input())
discount = int(input())

pen_price = 5.80
markers_price = 7.20
liquid_price = 1.20

pen_qty = pen_count * pen_price
markers_qty = markers_count * markers_price
liquid_qty = liquid_liters * liquid_price

total_materials_price = pen_qty + markers_qty + liquid_qty
total_price_discount = total_materials_price - (total_materials_price * discount/100)

print(total_price_discount)