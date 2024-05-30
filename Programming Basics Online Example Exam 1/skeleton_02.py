from math import floor

minutes = int(input())
seconds = int(input())
lenght = float(input())
seconds_per_100_meters = int(input())

total_time = minutes * 60 + seconds
delay_time = lenght/120
total_delay_time = delay_time * 2.5
marin_time = (lenght/100)*seconds_per_100_meters-total_delay_time

if marin_time <= total_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {marin_time-total_time:.3f} second slower.")