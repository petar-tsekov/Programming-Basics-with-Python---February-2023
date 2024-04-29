coins_001 = 0
coins_002 = 0
coins_005 = 0
coins_010 = 0
coins_020 = 0
coins_050 = 0
coins_1 = 0
coins_2 = 0
total_change_left = 0
change_entered = float(input())


while change_entered > 0:
    if change_entered >= 2:
        coins_2 += 1
        change_entered = round(change_entered - 2, 2)
    elif change_entered >= 1:
        coins_1 += 1
        change_entered = round(change_entered - 1, 2)
    elif change_entered >= 0.50:
        coins_050 += 1
        change_entered = round(change_entered - 0.50, 2)
    elif change_entered >= 0.20:
        coins_020 += 1
        change_entered = round(change_entered - 0.20, 2)
    elif change_entered >= 0.10:
        coins_010 += 1
        change_entered = round(change_entered - 0.10, 2)
    elif change_entered >= 0.05:
        coins_005 += 1
        change_entered = round(change_entered - 0.05, 2)
    elif change_entered >= 0.02:
        coins_002 += 1
        change_entered = round(change_entered - 0.02, 2)
    elif change_entered >= 0.01:
        coins_001 += 1
        change_entered = round(change_entered - 0.01, 2)

total_coins = coins_001 + coins_002 + coins_005 + coins_010 + coins_020 + coins_050 + coins_1 + coins_2

print(total_coins)