first_player_name = input()
second_player_name = input()

first_player_score = 0
second_player_score = 0
total_first_player_score = 0
total_second_player_score = 0

while True:
    first_player_command = input()
    if first_player_command == "End of game":
        print(f"{first_player_name} has {total_first_player_score} points")
        print(f"{second_player_name} has {total_second_player_score} points")
        break
    first_player_command_int = int(first_player_command)
    second_player_command = int(input())

    if first_player_command_int > second_player_command:
        first_player_score = first_player_command_int - second_player_command
        total_first_player_score += first_player_score
    elif second_player_command > first_player_command_int:
        second_player_score = second_player_command - first_player_command_int
        total_second_player_score += second_player_score
    elif first_player_command_int == second_player_command:
        print(f"Number wars!")
        first_player_command = int(input())
        second_player_command = int(input())
        if first_player_command > second_player_command:
            print(f"{first_player_name} is winner with {total_first_player_score} points")
        elif second_player_command > first_player_command:
            print(f"{second_player_name} is winner with {total_second_player_score} points")
        break

