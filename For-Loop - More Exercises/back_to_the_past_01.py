
starting_year = 1800
money_entered = float(input())
last_year = int(input())


ivan_age = 17
year_count = 0
money_left = 0
spend_money_odd = 0
spend_money_even = 0

for years in range(starting_year, last_year + 1):
    year_count += 1
    ivan_age += 1
    if years % 2 == 0:
        spend_money_even = spend_money_even - 12000
    else:
        spend_money = 12000 + 50 * ivan_age
        spend_money_odd = spend_money_odd - spend_money

money_left = abs(spend_money_even) + abs(spend_money_odd)

if money_left <= money_entered:
    print(f"Yes! He will live a carefree life and will have {money_entered - money_left:.2f} dollars left.")
else:
    print(f"He will need {money_left - money_entered:.2f} dollars to survive." )