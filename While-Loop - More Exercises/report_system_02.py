
money_needed = int(input())

command_entered = input()

days_count = 0
cash_money = 0
visa_money = 0
total_money = 0
cash_bills = 0
visa_bills = 0
while command_entered != "End":
    command_int = int(command_entered)
    days_count += 1

    if days_count % 2 == 0:
        if command_int >= 10:
            visa_money += command_int
            visa_bills += 1
            print(f"Product sold!")
        else:
            print(f"Error in transaction!")
    else:
        if command_int <= 100:
            cash_money += command_int
            cash_bills += 1
            print(f"Product sold!")
        else:
            print(f"Error in transaction!")
    total_money = visa_money + cash_money
    if total_money >= money_needed:
        print(f"Average CS: {cash_money/cash_bills:.2f}")
        print(f"Average CC: {visa_money/visa_bills:.2f}" )
        break

    command_entered = input()

else:
    print(f"Failed to collect required money for charity.")

"""
money_needed = int(input())



days_count = 0
cash_money = 0
visa_money = 0
total_money = 0
cash_bills = 0
visa_bills = 0
while True:
    command_entered = input()
    if command_entered == "End":
        print(f"Failed to collect required money for charity.")
        break
    command_int = int(command_entered)
    days_count += 1

    if days_count % 2 == 0:
        if command_int >= 10:
            visa_money += command_int
            visa_bills += 1
            print(f"Product sold!")
        else:
            print(f"Error in transaction!")
    else:
        if command_int <= 100:
            cash_money += command_int
            cash_bills += 1
            print(f"Product sold!")
        else:
            print(f"Error in transaction!")
    total_money = visa_money + cash_money
    if total_money >= money_needed:
        print(f"Average CS: {cash_money/cash_bills:.2f}")
        print(f"Average CC: {visa_money/visa_bills:.2f}" )
        break


"""