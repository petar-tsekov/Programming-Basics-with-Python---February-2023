
basketball_fee = int(input())

basketball_shoes = basketball_fee - (basketball_fee * 40/100)
basketball_shirt = basketball_shoes - (basketball_shoes * 20/100)
basketball_ball = basketball_shirt / 4
basketball_accessories = basketball_ball / 5

total_price = basketball_shoes + basketball_shirt + basketball_ball +  + basketball_accessories + basketball_fee

print(total_price)
