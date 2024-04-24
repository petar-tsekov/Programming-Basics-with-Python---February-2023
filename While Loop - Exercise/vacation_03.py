trip_money = float(input())
current_money = float(input())

days_spend = 0
total_days = 0
total_money = 0

while True:
    action = input()
    money_spend_save = float(input())

    if action == "spend":
        days_spend += 1
        total_days += 1

        current_money -= money_spend_save
        if current_money < 0:
            current_money = 0

        if days_spend == 5:
            print(f"You can't save the money.")
            print(total_days)
            break
    if action == "save":
        days_spend -= 1
        total_days += 1

        current_money += money_spend_save

        if current_money >= trip_money:
            print(f"You saved the money for {total_days} days.")
            break


