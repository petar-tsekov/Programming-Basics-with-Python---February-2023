
entered_number = int(input())

bonus_points = 0
total_number = 0

if entered_number <= 100:
    bonus_points = 5

elif 100 < entered_number < 1000:
    bonus_points = entered_number * 0.20

else:
    bonus_points = entered_number * 0.10

if entered_number % 2 == 0:
    bonus_points += 1

elif entered_number % 10 == 5:
    bonus_points += 2

total_number = entered_number + bonus_points

print(bonus_points)
print(total_number)



