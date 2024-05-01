soap_bottle_qty = int(input())
soap_bottle_capacity = 750
days_count = 0
plates_count = 0
pots_count = 0
plates_soap_used = 0
pots_soap_used = 0
total_soap = soap_bottle_capacity * soap_bottle_qty

while True:
    command = input()
    if command == "End":
        print(f"Detergent was enough!")
        print(f"{plates_count} dishes and {pots_count} pots were washed.")
        print(f"Leftover detergent {total_soap} ml.")
        break
    else:
        command_int = int(command)
    days_count += 1
    if days_count % 3 == 0:
        pots_count += command_int
        pots_soap_used = command_int * 15
        if pots_soap_used > total_soap:
            print(f"Not enough detergent, {pots_soap_used - total_soap} ml. more necessary!")
            break
        else:
            total_soap -= pots_soap_used

    else:
        plates_count += command_int
        plates_soap_used = command_int * 5
        if plates_soap_used > total_soap:
            print(f"Not enough detergent, {plates_soap_used - total_soap} ml. more necessary!")
            break
        else:
            total_soap -= plates_soap_used


"""soap_bottle_qty = int(input())
soap_bottle_capacity = 750
days_count = 0
plates_count = 0
pots_count = 0
plates_soap_used = 0
pots_soap_used = 0
total_soap = soap_bottle_capacity * soap_bottle_qty

command = input()

while command != "End":

    command_int = int(command)
    days_count += 1
    if days_count % 3 == 0:
        pots_count += command_int
        pots_soap_used = command_int * 15
        if pots_soap_used > total_soap:
            print(f"Not enough detergent, {pots_soap_used - total_soap} ml. more necessary!")
            break
        else:
            total_soap -= pots_soap_used

    else:
        plates_count += command_int
        plates_soap_used = command_int * 5
        if plates_soap_used > total_soap:
            print(f"Not enough detergent, {plates_soap_used - total_soap} ml. more necessary!")
            break
        else:
            total_soap -= plates_soap_used
    command = input()

else:
    print(f"Detergent was enough!")
    print(f"{plates_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {total_soap} ml.")







"""









