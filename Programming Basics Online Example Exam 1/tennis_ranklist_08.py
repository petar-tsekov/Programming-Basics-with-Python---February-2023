import math

tournament_qty = int(input())
starting_point = int(input())

win_points = 2000
finalits_points = 1200
semi_finalist_poinst = 720
total_points = 0
tournament_won = 0
percent_won_tournament = 0

for x in range(tournament_qty):
    tournament_position = input()

    if tournament_position == "W":
        tournament_won += 1
        starting_point += win_points
        total_points += win_points
    elif tournament_position == "F":
        starting_point += finalits_points
        total_points += finalits_points
    elif tournament_position == "SF":
        starting_point += semi_finalist_poinst
        total_points += semi_finalist_poinst

avarege_points = total_points / tournament_qty
percent_won_tournament = (tournament_won / tournament_qty) * 100

print(f"Final points: {starting_point}")
print(f"Average points: {math.floor(avarege_points)}")
print(f"{percent_won_tournament:.2f}%")