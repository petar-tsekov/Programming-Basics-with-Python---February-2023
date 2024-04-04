nylon_qty = int(input())
paint_qty = int(input())
liquid_qty = int(input())
working_hours = int(input())

nylon_price = 1.5
paint_price = 14.50
liquid_price = 5
extra_space = 2
bags = 0.40
paint_precent = 10


nylon_total = (nylon_qty + extra_space) * nylon_price
paint_total = (paint_qty + (paint_qty * paint_precent/100)) * paint_price
liquid_total = liquid_qty * liquid_price
total_materials_price = nylon_total + paint_total + liquid_total + bags
total_worker_price = (total_materials_price * 30/100) * working_hours
total_price = total_worker_price + total_materials_price

print(total_price)
