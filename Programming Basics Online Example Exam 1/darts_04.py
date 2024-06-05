player_name = input()
total_points = 301
plays_qty = 0
unsuccessful_try = 0


while True:
    command_entered = input()
    if command_entered == "Retire":
        print(f"{player_name} retired after {unsuccessful_try} unsuccessful shots.")
        break
    points_entered = int(input())
    current_points = 0

    if command_entered == "Single":
        current_points = points_entered
    elif command_entered == "Double":
        current_points = points_entered * 2
    elif command_entered == "Triple":
        current_points = points_entered * 3
    if current_points > total_points:
        unsuccessful_try += 1
        continue
    else:
        plays_qty += 1
    total_points = total_points - current_points

    if total_points == 0:
        print(f"{player_name} won the leg with {plays_qty} shots.")
        break
