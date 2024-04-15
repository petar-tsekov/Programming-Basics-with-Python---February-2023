
movie_type = input()
rows_seats = int(input())
cows_seats = int(input())

total_profit = 0

if movie_type == "Premiere":
    total_profit = rows_seats * cows_seats * 12
elif movie_type == "Normal":
    total_profit = rows_seats * cows_seats * 7.50
elif movie_type == "Discount":
    total_profit = rows_seats * cows_seats * 5

print(f"{total_profit:.2f} leva")
