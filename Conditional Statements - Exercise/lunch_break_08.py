import math

movie_name = input()
episode_duration = int(input())
lunch_break = int(input())

eating_time = lunch_break * 1/8
time_to_relax = lunch_break * 1/4
time_left = lunch_break - eating_time - time_to_relax

if time_left >= episode_duration:
    rest_time = math.ceil(time_left - episode_duration)
    print(f"You have enough time to watch {movie_name} and left with {rest_time} minutes free time.")
else:
    needed_time = math.ceil(episode_duration - time_left)
    print(f"You don't have enough time to watch {movie_name}, you need {needed_time} more minutes.")