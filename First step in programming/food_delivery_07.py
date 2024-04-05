
chicken_menu_qty = int(input())
fish_menu_qty = int(input())
vegan_menu_qty = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery_price = 2.50

chicken_menu_total = chicken_menu_qty * chicken_menu_price
fish_menu_total = fish_menu_qty * fish_menu_price
vegan_menu_total = vegan_menu_price * vegan_menu_qty
total_menu_price = chicken_menu_total + fish_menu_total + vegan_menu_total
desert_price = total_menu_price - (total_menu_price - (total_menu_price * 20/100))

total_price = total_menu_price + desert_price + delivery_price
print(total_price)