intervals_count = int(input())
total_points = 0

zero_nine_number = 0
ten_19_number = 0
twenty_29_number = 0
thirty_39_number = 0
forty_49_number = 0
unvalid_number = 0
for intervals in range(intervals_count):
    number_entered = int(input())


    if 0 <= number_entered <= 9:
        total_points += number_entered * 0.20
        zero_nine_number += 1
    elif 10 <= number_entered <= 19:
        total_points += number_entered * 0.30
        ten_19_number += 1
    elif 20 <= number_entered <= 29:
        total_points += number_entered * 0.40
        twenty_29_number += 1
    elif 30 <= number_entered <= 39:
        total_points += 50
        thirty_39_number += 1
    elif 40 <= number_entered <= 50:
        total_points += 100
        forty_49_number += 1
    else:
        total_points /= 2
        unvalid_number += 1


print(f"{total_points:.2f}")
print(f"From 0 to 9: {zero_nine_number/intervals_count * 100:.2f}%")
print(f"From 10 to 19: {ten_19_number/intervals_count * 100:.2f}%")
print(f"From 20 to 29: {twenty_29_number/intervals_count * 100:.2f}%")
print(f"From 30 to 39: {thirty_39_number/intervals_count * 100:.2f}%")
print(f"From 40 to 50: {forty_49_number/intervals_count * 100:.2f}%")
print(f"Invalid numbers: {unvalid_number/intervals_count * 100:.2f}%")