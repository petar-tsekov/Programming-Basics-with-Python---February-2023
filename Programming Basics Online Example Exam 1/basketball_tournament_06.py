tournament_name = input()
matches_played = 0
matches_won = 0
matches_lost = 0

while tournament_name != "End of tournaments":
    tournament_matches = int(input())
    matches_played += tournament_matches

    for matches in range(1, tournament_matches + 1):
        home_team_score = int(input())
        away_team_score = int(input())

        if home_team_score > away_team_score:
            matches_won +=1
            print(f"Game {matches} of tournament {tournament_name}: win with {home_team_score-away_team_score} points.")
        else:
            matches_lost += 1
            print(f"Game {matches} of tournament {tournament_name}: lost with {away_team_score-home_team_score} points.")

    tournament_name = input()

else:
    print(f"{matches_won/matches_played * 100:.2f}% matches win")
    print(f"{matches_lost/matches_played * 100:.2f}% matches lost")