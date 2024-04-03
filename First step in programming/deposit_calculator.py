

deposit_sum = float(input())
deposit_term = int(input())
percent_rating = float(input())

total_sum = deposit_sum + deposit_term * ((deposit_sum * percent_rating/100) / 12)


print(total_sum)