import math

record_in_second = float(input())
distance_in_metars = float(input())
time_for_one_metar = float(input())

resistance_distance = 15
resitance_time = 12.5

total_distance = distance_in_metars * time_for_one_metar
additional_distance = math.floor(distance_in_metars/resistance_distance) * resitance_time
total_time = total_distance + additional_distance

if total_time < record_in_second:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

else:
    total_time = total_time - record_in_second
    print(f"No, he failed! He was {total_time:.2f} seconds slower.")
